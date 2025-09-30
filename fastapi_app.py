from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional

from task_2.prompt import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

app = FastAPI(
    title="DebateBot API",
    description="AI-powered debate conversation API",
    version="1.0.0",
)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# In-memory conversation storage
conversations = {}


class ChatRequest(BaseModel):
    conversation_id: Optional[str] = None
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "conversation_id": None,
                "message": "Let's debate: Climate change is real and urgent. You argue FOR this position.",
            }
        }


class MessageItem(BaseModel):
    role: str
    message: str


class ChatResponse(BaseModel):
    conversation_id: str
    message: list[MessageItem]


def extract_topic_and_side(message: str):
    """Extract topic and side from the first message using OpenAI"""
    try:
        extraction_prompt = """Analyze this message and extract:
1. The debate topic
2. What side the bot should argue (pro/for or con/against)

Message: "{message}"

Respond in this exact format:
TOPIC: [the debate topic]
SIDE: [pro or con]"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that extracts debate topics and positions from messages.",
                },
                {"role": "user", "content": extraction_prompt.format(message=message)},
            ],
            max_tokens=100,
            temperature=0.3,
        )

        result = response.choices[0].message.content

        # Parse the response
        topic = "the given topic"
        side = "pro"

        for line in result.split("\n"):
            if line.startswith("TOPIC:"):
                topic = line.replace("TOPIC:", "").strip()
            elif line.startswith("SIDE:"):
                side_text = line.replace("SIDE:", "").strip().lower()
                side = "pro" if "pro" in side_text or "for" in side_text else "con"

        return topic, side

    except Exception as e:
        # Default fallback
        return "the given topic", "pro"


def generate_debate_response(
    user_message: str, topic: str, side: str, conversation_history: list
):
    """Generate AI response for debate"""
    try:
        # Format the system prompt with topic and side
        system_prompt = SYSTEM_PROMPT.format(topic=topic, side=side)

        # Prepare messages for OpenAI
        messages = [{"role": "system", "content": system_prompt}]

        # Add conversation history
        for msg in conversation_history:
            # Convert 'bot' role to 'assistant' for OpenAI API
            role = "assistant" if msg["role"] == "bot" else msg["role"]
            messages.append({"role": role, "content": msg["message"]})

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
        return f"I apologize, but I'm having trouble generating a response right now. Error: {str(e)}"


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat with the debate bot.

    **Starting a new conversation (first message):**
    - Set `conversation_id` to `null`
    - The `message` should define the debate topic and what side the bot should argue
    - Example: "Let's debate: Climate change is real. You argue FOR this position."

    **Continuing a conversation:**
    - Include the `conversation_id` from the previous response
    - Send your debate message

    Returns the conversation_id and the 5 most recent message pairs.
    """
    try:
        user_message = request.message
        conversation_id = request.conversation_id

        # Check if this is a new conversation (no conversation_id)
        if not conversation_id:
            # New conversation - extract topic and side from first message
            conversation_id = str(uuid.uuid4())

            # Extract topic and side from the user's first message
            topic, side = extract_topic_and_side(user_message)

            # Initialize conversation
            conversations[conversation_id] = {
                "topic": topic,
                "side": side,
                "history": [],
            }

        # Get conversation data
        if conversation_id not in conversations:
            raise HTTPException(status_code=404, detail="Conversation not found")

        conversation = conversations[conversation_id]
        topic = conversation["topic"]
        side = conversation["side"]
        history = conversation["history"]

        # Add user message to history
        user_msg = {"role": "user", "message": user_message}
        history.append(user_msg)

        # Generate bot response
        bot_response = generate_debate_response(
            user_message,
            topic,
            side,
            history[:-1],  # Exclude the just-added user message
        )

        # Add bot response to history
        bot_msg = {"role": "bot", "message": bot_response}
        history.append(bot_msg)

        # Keep only the 5 most recent messages (5 exchanges = 10 messages)
        # Return last 10 messages (5 user + 5 bot pairs)
        recent_messages = history[-10:] if len(history) > 10 else history

        return ChatResponse(
            conversation_id=conversation_id,
            message=[MessageItem(**msg) for msg in recent_messages],
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/")
async def root():
    return {"message": "Hello, DebateBot here!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
