# 🤖 DebateBot Pro

An intelligent AI-powered debate application built with Streamlit and OpenAI. Engage in meaningful debates with an AI that can argue from different perspectives on any topic.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://debate-chatbot.streamlit.app/)

<a href="https://youtu.be/YOUR_DEMO_VIDEO_LINK" target="_blank" rel="noopener">
  <svg xmlns="http://www.w3.org/2000/svg" id="yt-ringo2-svg_yt9" width="93" height="20" viewBox="0 0 93 20" focusable="false" aria-hidden="true" style="pointer-events: none; display: inherit; width: 30%; height: 30%;">
    <g>
      <path d="M14.4848 20C14.4848 20 23.5695 20 25.8229 19.4C27.0917 19.06 28.0459 18.08 28.3808 16.87C29 14.65 29 9.98 29 9.98C29 9.98 29 5.34 28.3808 3.14C28.0459 1.9 27.0917 0.94 25.8229 0.61C23.5695 0 14.4848 0 14.4848 0C14.4848 0 5.42037 0 3.17711 0.61C1.9286 0.94 0.954148 1.9 0.59888 3.14C0 5.34 0 9.98 0 9.98C0 9.98 0 14.65 0.59888 16.87C0.954148 18.08 1.9286 19.06 3.17711 19.4C5.42037 20 14.4848 20 14.4848 20Z" fill="#FF0033"></path>
      <path d="M19 10L11.5 5.75V14.25L19 10Z" fill="white"></path>
    </g>
    <g id="youtube-paths_yt9">
      <path d="M37.1384 18.8999V13.4399L40.6084 2.09994H38.0184L36.6984 7.24994C36.3984 8.42994 36.1284 9.65994 35.9284 10.7999H35.7684C35.6584 9.79994 35.3384 8.48994 35.0184 7.22994L33.7384 2.09994H31.1484L34.5684 13.4399V18.8999H37.1384Z"></path>
      <path d="M44.1003 6.29994C41.0703 6.29994 40.0303 8.04994 40.0303 11.8199V13.6099C40.0303 16.9899 40.6803 19.1099 44.0403 19.1099C47.3503 19.1099 48.0603 17.0899 48.0603 13.6099V11.8199C48.0603 8.44994 47.3803 6.29994 44.1003 6.29994ZM45.3903 14.7199C45.3903 16.3599 45.1003 17.3899 44.0503 17.3899C43.0203 17.3899 42.7303 16.3499 42.7303 14.7199V10.6799C42.7303 9.27994 42.9303 8.02994 44.0503 8.02994C45.2303 8.02994 45.3903 9.34994 45.3903 10.6799V14.7199Z"></path>
      <path d="M52.2713 19.0899C53.7313 19.0899 54.6413 18.4799 55.3913 17.3799H55.5013L55.6113 18.8999H57.6012V6.53994H54.9613V16.4699C54.6812 16.9599 54.0312 17.3199 53.4212 17.3199C52.6512 17.3199 52.4113 16.7099 52.4113 15.6899V6.53994H49.7812V15.8099C49.7812 17.8199 50.3613 19.0899 52.2713 19.0899Z"></path>
      <path d="M62.8261 18.8999V4.14994H65.8661V2.09994H57.1761V4.14994H60.2161V18.8999H62.8261Z"></path>
      <path d="M67.8728 19.0899C69.3328 19.0899 70.2428 18.4799 70.9928 17.3799H71.1028L71.2128 18.8999H73.2028V6.53994H70.5628V16.4699C70.2828 16.9599 69.6328 17.3199 69.0228 17.3199C68.2528 17.3199 68.0128 16.7099 68.0128 15.6899V6.53994H65.3828V15.8099C65.3828 17.8199 65.9628 19.0899 67.8728 19.0899Z"></path>
      <path d="M80.6744 6.26994C79.3944 6.26994 78.4744 6.82994 77.8644 7.73994H77.7344C77.8144 6.53994 77.8744 5.51994 77.8744 4.70994V1.43994H75.3244L75.3144 12.1799L75.3244 18.8999H77.5444L77.7344 17.6999H77.8044C78.3944 18.5099 79.3044 19.0199 80.5144 19.0199C82.5244 19.0199 83.3844 17.2899 83.3844 13.6099V11.6999C83.3844 8.25994 82.9944 6.26994 80.6744 6.26994ZM80.7644 13.6099C80.7644 15.9099 80.4244 17.2799 79.3544 17.2799C78.8544 17.2799 78.1644 17.0399 77.8544 16.5899V9.23994C78.1244 8.53994 78.7244 8.02994 79.3944 8.02994C80.4744 8.02994 80.7644 9.33994 80.7644 11.7299V13.6099Z"></path>
      <path d="M92.6517 11.4999C92.6517 8.51994 92.3517 6.30994 88.9217 6.30994C85.6917 6.30994 84.9717 8.45994 84.9717 11.6199V13.7899C84.9717 16.8699 85.6317 19.1099 88.8417 19.1099C91.3817 19.1099 92.6917 17.8399 92.5417 15.3799L90.2917 15.2599C90.2617 16.7799 89.9117 17.3999 88.9017 17.3999C87.6317 17.3999 87.5717 16.1899 87.5717 14.3899V13.5499H92.6517V11.4999ZM88.8617 7.96994C90.0817 7.96994 90.1717 9.11994 90.1717 11.0699V12.0799H87.5717V11.0699C87.5717 9.13994 87.6517 7.96994 88.8617 7.96994Z"></path>
    </g>
  </svg>
</a>


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

- **`OPENAI_MODEL`**: OpenAI model to use (default: `gpt-5-nano`)
  - Available: `gpt-5-nano`, `gpt-4`, `gpt-4-turbo-preview`
- **`API_TIMEOUT`**: API timeout in seconds (default: `10`)
- **`STREAMLIT_SERVER_PORT`**: Server port (default: `8501`)
- **`STREAMLIT_SERVER_ADDRESS`**: Server address (default: `0.0.0.0`)
- **`ENVIRONMENT`**: Environment mode (default: `production`)
- **`LOG_LEVEL`**: Log level (default: `INFO`)

### Example .env file:
```bash
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_MODEL=gpt-5-nano
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
   - Try using `gpt-5-nano` instead of `gpt-4`
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
