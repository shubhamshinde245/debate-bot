# DebateBot FastAPI

A FastAPI-based debate bot API with automatic interactive documentation. The bot uses AI to engage in intelligent debates, automatically extracting the topic and position from your first message.

## Features

- 🚀 FastAPI with automatic Swagger UI documentation
- 🤖 AI-powered debate responses using OpenAI GPT
- 💬 Conversation management with unique IDs
- 📝 Returns 5 most recent message pairs
- 🎯 Automatic topic and side extraction from first message
- ⚡ Fast and async request handling

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Create a `.env` file with your OpenAI API key:**
```
OPENAI_API_KEY=your_api_key_here
```

3. **Run the FastAPI app:**
```bash
python fastapi_app.py
```

The API will be available at `http://localhost:8000`

## Interactive Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: `http://localhost:8000/docs` (Interactive, try it out!)
- **ReDoc**: `http://localhost:8000/redoc` (Alternative docs)

## API Endpoints

### POST `/chat`

Chat with the debate bot.

**Request Format:**
```json
{
    "conversation_id": "string | null",
    "message": "string"
}
```

**Response Format:**
```json
{
    "conversation_id": "string",
    "message": [
        {
            "role": "user",
            "message": "string"
        },
        {
            "role": "bot",
            "message": "string"
        }
    ]
}
```

**Note:** Response contains the 5 most recent message pairs (up to 10 messages total).

### GET `/health`

Health check endpoint.

**Response:**
```json
{
    "status": "healthy"
}
```

### GET `/`

Root endpoint.

**Response:**
```json
{
    "message": "Hello, DebateBot here!"
}
```

## Usage Examples

### Test Case 1: Starting a New Conversation (Climate Change Debate)

**Request:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": null,
    "message": "Let'\''s debate: Climate change is real and urgent. You argue FOR this position."
  }'
```

**Response:**
```json
{
  "conversation_id": "3ffb8f8e-52f9-4bef-887c-466eb0d89b13",
  "message": [
    {
      "role": "user",
      "message": "Let's debate: Climate change is real and urgent. You argue FOR this position."
    },
    {
      "role": "bot",
      "message": "Absolutely, I'm glad you brought up this crucial topic. Climate change is indeed real and urgent. The scientific consensus is overwhelming in support of this fact. Have you considered the extensive research done by climate scientists worldwide that shows the significant impact human activities have had on our planet's climate?\n\nIt's not just about rising global temperatures; it's also about the increasing frequency of extreme weather events like hurricanes, droughts, and wildfires. These events not only pose immediate dangers to human lives and infrastructure but also have long-term consequences for ecosystems and biodiversity. How do you interpret these observable changes in our environment?"
    }
  ]
}
```

### Test Case 2: Continuing the Conversation

**Request:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "3ffb8f8e-52f9-4bef-887c-466eb0d89b13",
    "message": "I think its just an excuse humans are making because they are lazy"
  }'
```

**Response:**
```json
{
  "conversation_id": "3ffb8f8e-52f9-4bef-887c-466eb0d89b13",
  "message": [
    {
      "role": "user",
      "message": "Let's debate: Climate change is real and urgent. You argue FOR this position."
    },
    {
      "role": "bot",
      "message": "Absolutely, I'm glad you brought up this crucial topic. Climate change is indeed real and urgent. The scientific consensus is overwhelming in support of this fact. Have you considered the extensive research done by climate scientists worldwide that shows the significant impact human activities have had on our planet's climate?\n\nIt's not just about rising global temperatures; it's also about the increasing frequency of extreme weather events like hurricanes, droughts, and wildfires. These events not only pose immediate dangers to human lives and infrastructure but also have long-term consequences for ecosystems and biodiversity. How do you interpret these observable changes in our environment?"
    },
    {
      "role": "user",
      "message": "I think its just an excuse humans are making because they are lazy"
    },
    {
      "role": "bot",
      "message": "I understand your skepticism, and I appreciate you sharing that perspective. However, let me offer a different interpretation. The notion that climate change is merely an excuse doesn't align with the rigorous scientific methodology that has been employed for decades to study our planet's climate systems.\n\nConsider this: Thousands of independent scientists from different countries, backgrounds, and institutions have all arrived at similar conclusions through peer-reviewed research. These aren't lazy individuals—they're dedicated researchers who've spent years analyzing ice cores, atmospheric data, ocean temperatures, and countless other metrics. What would motivate such a diverse global community to fabricate or exaggerate findings?\n\nMoreover, we can observe tangible evidence ourselves: Glaciers that existed for millennia are disappearing, sea levels are measurably rising, and we're experiencing unprecedented temperature records. These aren't abstract concepts—they're measurable, documented changes. How would human laziness explain these concrete physical transformations in our environment?"
    }
  ]
}
```

## How the Bot Works

### Starting a Conversation

When you send the first message with `conversation_id: null`, the bot:

1. **Extracts Topic and Side**: Uses AI to analyze your message and identify:
   - The debate topic
   - What position the bot should take (pro/for or con/against)

2. **Creates Conversation**: Generates a unique `conversation_id` and stores the conversation context

3. **Responds**: Generates an AI response advocating for the assigned position

**Example first messages:**
- `"Let's debate: Climate change is real and urgent. You argue FOR this position."`
- `"Debate topic: AI will replace human jobs. Take the AGAINST position."`
- `"I want to discuss universal basic income. You support it (PRO side)."`

### Continuing a Conversation

Include the `conversation_id` from the previous response to continue the debate:

- The bot remembers the topic and its position
- All previous messages are maintained in context
- The bot stays in character and defends its assigned position
- Returns the 5 most recent message exchanges

## Message History

- The API stores the **complete conversation history** internally
- Each response returns the **5 most recent message pairs** (10 messages total)
- This keeps responses manageable while maintaining conversation context

## Bot Behavior

The bot is programmed to:

- ✅ **Stay on topic**: Redirects if the conversation drifts
- ✅ **Maintain position**: Never concedes its core argument
- ✅ **Use academic tone**: Friendly yet intellectually rigorous
- ✅ **Ask questions**: Uses Socratic method to engage
- ✅ **Acknowledge counterpoints**: Respects opposing views while reframing
- ✅ **End with engagement**: Concludes with calls to continue discussion

## Testing with Swagger UI

1. Open `http://localhost:8000/docs`
2. Click on `/chat` endpoint
3. Click "Try it out"
4. Enter your request JSON:
   ```json
   {
     "conversation_id": null,
     "message": "Let's debate: Social media does more harm than good. Argue AGAINST this."
   }
   ```
5. Click "Execute"
6. Copy the `conversation_id` from the response
7. Try another request with the same `conversation_id` to continue

## Configuration

### AI Model Settings

The bot uses OpenAI's GPT-3.5-turbo with these parameters (in `fastapi_app.py`):

```python
model="gpt-3.5-turbo"
max_tokens=500
temperature=0.7
presence_penalty=0.6
frequency_penalty=0.3
```

### System Prompt

The bot's personality and behavior are defined by `SYSTEM_PROMPT` in `task_2/prompt.py`. You can customize:
- Tone and character
- Debate strategy
- Topic adherence rules
- Conversation style

## Error Handling

The API provides clear error messages:

- **400 Bad Request**: Missing required fields
- **404 Not Found**: Invalid conversation_id
- **500 Internal Server Error**: API or processing errors

## Production Considerations

For production deployment:

1. **Persistent Storage**: Replace in-memory `conversations` dict with a database (Redis, PostgreSQL, etc.)
2. **Authentication**: Add API keys or OAuth
3. **Rate Limiting**: Implement request throttling
4. **Logging**: Add comprehensive logging for debugging
5. **CORS**: Configure CORS for web clients
6. **Environment**: Use production ASGI server (Gunicorn + Uvicorn workers)

## Technical Details

- **Framework**: FastAPI 0.115.0
- **ASGI Server**: Uvicorn
- **AI Model**: OpenAI GPT-3.5-turbo
- **Data Validation**: Pydantic v2
- **Storage**: In-memory (dict)

## License

This project is for educational and demonstration purposes.