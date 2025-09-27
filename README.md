# 🤖 DebateBot Pro

An intelligent AI-powered debate application built with Streamlit and FastAPI. Engage in meaningful debates with an AI that can argue from different perspectives on any topic.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app/)

## ✨ Features

- 🤖 **AI-Powered Arguments**: Uses OpenAI's GPT models for intelligent debate responses
- 🎯 **Customizable Topics**: Debate any topic you choose
- ⚖️ **Flexible Positions**: Choose whether the bot argues 'pro' or 'con'
- 💾 **Conversation Memory**: Maintains context throughout the debate
- 🎨 **Beautiful Interface**: Modern, responsive UI with smooth animations
- ☁️ **Cloud Ready**: Works both locally and on Streamlit Cloud

## 🚀 Quick Start

### Prerequisites

1. **Python 3.8+** installed on your system
2. **OpenAI API Key** - Get one from [OpenAI Platform](https://platform.openai.com/api-keys)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd debate-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```bash
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```
   
   Replace `your_openai_api_key_here` with your actual OpenAI API key.

### Running the Application

#### Option 1: Integrated Mode (Recommended for Streamlit Cloud)
```bash
streamlit run streamlit_app.py
```

#### Option 2: Separate API Server (For local development)
```bash
# Terminal 1: Start the API server
python api_server.py

# Terminal 2: Start the Streamlit app
streamlit run streamlit_app.py
```

#### Option 3: Using the startup script
```bash
# Start just the Streamlit app (integrated mode)
python start.py streamlit

# Start just the API server
python start.py api

# Get help for both modes
python start.py both
```

## 🌐 Deployment to Streamlit Cloud

1. **Push your code to GitHub**
2. **Connect to Streamlit Cloud** and deploy your repository
3. **Add your OpenAI API key** as a secret in Streamlit Cloud:
   - Go to your app settings
   - Add secret: `OPENAI_API_KEY` = `your_api_key_here`
4. **Deploy!** The app will automatically use integrated mode

## 🎮 How to Use

1. **Choose a Topic**: Enter your debate topic in the sidebar
2. **Pick Bot's Position**: Select whether the bot argues 'pro' or 'con'
3. **Start Debating**: Type your argument and hit send!
4. **Continue the Conversation**: The AI will respond with compelling arguments from its chosen position

## 🏗️ Architecture

- **Frontend**: Streamlit app with beautiful UI
- **Backend**: FastAPI server (optional) or integrated AI processing
- **AI**: OpenAI GPT models for intelligent responses
- **Memory**: In-memory conversation storage (can be extended to use databases)

## 📁 Project Structure

```
debate-bot/
├── streamlit_app.py      # Main Streamlit application
├── api_server.py         # FastAPI server (optional)
├── start.py              # Startup script
├── requirements.txt      # Python dependencies
├── task_2/
│   ├── models.py         # Pydantic models
│   └── prompt.py         # AI system prompts
└── README.md
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: OpenAI model to use (default: gpt-3.5-turbo)
- `API_TIMEOUT`: API timeout in seconds (default: 10)

### Customization

- **AI Personality**: Modify `task_2/prompt.py` to change how the AI debates
- **UI Styling**: Update the CSS in `streamlit_app.py`
- **Models**: Change the AI model in the `generate_debate_response` function

## 🐛 Troubleshooting

### Common Issues

1. **"Cannot connect to API server"**
   - The app automatically falls back to integrated mode
   - Make sure your OpenAI API key is set correctly

2. **"OPENAI_API_KEY environment variable is required"**
   - Create a `.env` file with your API key
   - For Streamlit Cloud, add it as a secret

3. **Slow responses**
   - Try using `gpt-3.5-turbo` instead of `gpt-4`
   - Check your OpenAI API usage limits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for providing the AI models
- Streamlit for the amazing web framework
- FastAPI for the robust API framework
