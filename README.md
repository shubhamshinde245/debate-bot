# 🤖 DebateBot Pro

An intelligent AI-powered debate application built with Streamlit and OpenAI. Engage in meaningful debates with an AI that can argue from different perspectives on any topic.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://debate-chatbot.streamlit.app/)


## ✨ Features

- 🤖 **AI-Powered Arguments**: Uses OpenAI's GPT models for intelligent debate responses
- 🎯 **Customizable Topics**: Debate any topic you choose
- ⚖️ **Flexible Positions**: Choose whether the bot argues 'pro' or 'con'
- 💾 **Conversation Memory**: Maintains context throughout the debate
- 🎨 **Beautiful Interface**: Modern, responsive UI with smooth animations
- 🐳 **Docker Ready**: Full containerization support for easy deployment
- ☁️ **Cloud Ready**: Works both locally and on Streamlit Cloud
- [**Technical Architecture & Design Decisions**](DECISION.md) — Deep dive into the system architecture, component breakdowns, and the rationale behind key engineering choices.


## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** or **Docker** installed on your system
- **OpenAI API Key** - Get one from [OpenAI Platform](https://platform.openai.com/api-keys)

### Option 1: Using Make (Recommended)

The easiest way to get started is using the provided Makefile:

```bash
# Clone the repository
git clone <your-repo-url>
cd debate-bot

# Quick setup (installs dependencies and creates .env file)
make quickstart

# Edit .env file with your OpenAI API key
# Then run in development mode
make dev

# Or run with Docker
make run
```

### Option 2: Manual Setup

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
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   # Development mode
   python start.py
   
   # Or directly with Streamlit
   streamlit run streamlit_app.py
   ```

### Option 3: Docker Deployment

```bash
# Build and run with Docker Compose
make run

# Or manually
docker-compose up -d
```

The application will be available at `http://localhost:8501`

## 🛠️ Available Make Commands

The project includes a comprehensive Makefile for easy development and deployment:

```bash
# Show all available commands
make help

# Setup & Installation
make install      # Install all requirements and dependencies
make check-deps   # Check if all required tools are installed
make setup-env    # Create .env file from template

# Testing
make test         # Run all tests

# Running
make run          # Run the service using Docker Compose
make dev          # Run in development mode (local Python)

# Management
make down         # Stop all running services
make clean        # Stop and remove all containers and volumes
make logs         # Show logs from running services

# Utilities
make lint         # Run code linting
make format       # Format code
make build        # Build Docker images
```

## 🔧 Environment Variables

The application uses environment variables for configuration. Copy `.env.example` to `.env` and configure:

### Required Variables

- **`OPENAI_API_KEY`**: Your OpenAI API key (required)
  - Get from: https://platform.openai.com/api-keys
  - Example: `sk-...`

### Optional Variables

- **`OPENAI_MODEL`**: OpenAI model to use (default: `gpt-3.5-turbo`)
  - Available: `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo-preview`
- **`API_TIMEOUT`**: API timeout in seconds (default: `10`)
- **`STREAMLIT_SERVER_PORT`**: Server port (default: `8501`)
- **`STREAMLIT_SERVER_ADDRESS`**: Server address (default: `0.0.0.0`)
- **`ENVIRONMENT`**: Environment mode (default: `production`)
- **`LOG_LEVEL`**: Log level (default: `INFO`)

### Example .env file:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
API_TIMEOUT=10
ENVIRONMENT=development
LOG_LEVEL=DEBUG
```

## 🌐 Deployment to Streamlit Cloud

1. **Push your code to GitHub**
2. **Connect to Streamlit Cloud** and deploy your repository
3. **Add your OpenAI API key** as a secret in Streamlit Cloud:
   - Go to your app settings
   - Add secret: `OPENAI_API_KEY` = `your_api_key_here`
4. **Deploy!** The app uses integrated AI processing

## 🎮 How to Use

1. **Choose a Topic**: Enter your debate topic in the sidebar
2. **Pick Bot's Position**: Select whether the bot argues 'pro' or 'con'
3. **Start Debating**: Type your argument and hit send!
4. **Continue the Conversation**: The AI will respond with compelling arguments from its chosen position

## 🏗️ Architecture

- **Frontend**: Streamlit app with beautiful UI
- **AI Processing**: Integrated OpenAI GPT models for intelligent responses
- **Memory**: In-memory conversation storage (can be extended to use databases)
- **Containerization**: Full Docker support with Docker Compose
- **Deployment**: Ready for local development, Docker, and cloud deployment

## 📁 Project Structure

```
debate-bot/
├── streamlit_app.py      # Main Streamlit application
├── start.py              # Startup script
├── requirements.txt      # Python dependencies
├── Makefile              # Development and deployment commands
├── Dockerfile            # Docker container configuration
├── docker-compose.yml    # Multi-service Docker setup
├── .env.example          # Environment variables template
├── .dockerignore         # Docker build exclusions
├── task_2/
│   ├── models.py         # Pydantic models
│   └── prompt.py         # AI system prompts
├── test_app.py           # Test suite
└── README.md
```

## 🔧 Configuration

### Customization

- **AI Personality**: Modify `task_2/prompt.py` to change how the AI debates
- **UI Styling**: Update the CSS in `streamlit_app.py`
- **Models**: Change the AI model in the `generate_debate_response` function
- **Docker**: Modify `Dockerfile` or `docker-compose.yml` for custom deployment

## 🐛 Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY environment variable is required"**
   - Run `make setup-env` to create `.env` file
   - Edit `.env` and set your API key
   - For Streamlit Cloud, add it as a secret

2. **Docker issues**
   - Run `make check-deps` to verify Docker installation
   - Try `make clean` then `make run` to rebuild
   - Check logs with `make logs`

3. **Slow responses**
   - Try using `gpt-3.5-turbo` instead of `gpt-4`
   - Check your OpenAI API usage limits
   - Increase `API_TIMEOUT` in `.env` if needed

4. **Port conflicts**
   - Change `STREAMLIT_SERVER_PORT` in `.env`
   - Or modify port mapping in `docker-compose.yml`

5. **Permission issues (Docker)**
   - Ensure Docker daemon is running
   - On Linux, add your user to docker group: `sudo usermod -aG docker $USER`

## 🛠️ Development

### Local Development

```bash
# Install dependencies
make install

# Run tests
make test

# Start development server
make dev

# Format code
make format

# Run linting
make lint
```

### Docker Development

```bash
# Build and run
make run

# View logs
make logs

# Stop services
make down

# Clean everything
make clean
```

### Testing

The project includes comprehensive tests:

```bash
# Run all tests
make test

# Or run directly
python test_app.py
```

Tests cover:
- Module imports
- Environment configuration
- Pydantic models
- Basic functionality

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
