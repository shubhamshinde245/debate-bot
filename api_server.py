# --- FastAPI Server for DebateBot ---
import os
import uuid
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
from task_2.models import ChatRequest, Message, ChatResponse
from task_2.prompt import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="DebateBot API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your Streamlit Cloud domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

# In-memory storage for conversations (in production, use a database)
conversations: Dict[str, List[Message]] = {}


def get_openai_client():
    """Get OpenAI client with proper configuration"""
    from openai import OpenAI

    return OpenAI(api_key=openai.api_key)


def generate_debate_response(
    user_message: str,
    topic: Optional[str],
    side: str,
    conversation_history: List[Message],
) -> str:
    """Generate AI response for debate"""
    try:
        client = get_openai_client()

        # Format the system prompt with topic and side
        system_prompt = SYSTEM_PROMPT.format(
            topic=topic or "the given topic", side=side
        )

        # Prepare messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]

        # Add conversation history
        for msg in conversation_history:
            messages.append({"role": msg.role, "content": msg.message})

        # Add the current user message
        messages.append({"role": "user", "content": user_message})

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7,
            presence_penalty=0.6,
            frequency_penalty=0.3,
        )

        return response.choices[0].message.content

    except Exception as e:
        print(f"Error generating response: {e}")
        return f"I apologize, but I'm having trouble generating a response right now. Error: {str(e)}"


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "DebateBot API is running!", "status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint for debate conversations"""
    try:
        # Get or create conversation
        conversation_id = request.conversation_id or str(uuid.uuid4())

        # Get existing conversation or create new one
        if conversation_id not in conversations:
            conversations[conversation_id] = []

        conversation_history = conversations[conversation_id]

        # Add user message to conversation
        user_message = Message(role="user", message=request.message)
        conversation_history.append(user_message)

        # Generate AI response
        ai_response = generate_debate_response(
            request.message,
            request.topic,
            request.side or "pro",
            conversation_history[:-1],  # Exclude the just-added user message
        )

        # Add AI response to conversation
        bot_message = Message(role="assistant", message=ai_response)
        conversation_history.append(bot_message)

        # Return response
        return ChatResponse(
            conversation_id=conversation_id, message=conversation_history
        )

    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/conversations/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get conversation history"""
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found")

    return {
        "conversation_id": conversation_id,
        "messages": conversations[conversation_id],
    }


@app.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: str):
    """Delete a conversation"""
    if conversation_id not in conversations:
        raise HTTPException(status_code=404, detail="Conversation not found")

    del conversations[conversation_id]
    return {"message": "Conversation deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
