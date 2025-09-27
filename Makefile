# DebateBot Pro - Makefile
# This Makefile provides convenient commands for development, testing, and deployment

.PHONY: help install test run down clean check-deps check-python check-docker check-env setup-env

# Default target - show help
help:
	@echo "🤖 DebateBot Pro - Available Commands"
	@echo "======================================"
	@echo ""
	@echo "📦 Setup & Installation:"
	@echo "  make install     - Install all requirements and dependencies"
	@echo "  make check-deps  - Check if all required tools are installed"
	@echo "  make setup-env   - Create .env file from template"
	@echo ""
	@echo "🧪 Testing:"
	@echo "  make test        - Run all tests"
	@echo ""
	@echo "🚀 Running:"
	@echo "  make run         - Run the service using Docker Compose"
	@echo "  make dev         - Run in development mode (local Python)"
	@echo ""
	@echo "🛑 Management:"
	@echo "  make down        - Stop all running services"
	@echo "  make clean       - Stop and remove all containers and volumes"
	@echo "  make logs        - Show logs from running services"
	@echo ""
	@echo "🔧 Utilities:"
	@echo "  make lint        - Run code linting"
	@echo "  make format      - Format code"
	@echo "  make build       - Build Docker images"

# Check dependencies
check-deps: check-python check-docker check-env
	@echo "✅ All dependencies check passed!"

check-python:
	@echo "🐍 Checking Python installation..."
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "❌ Python 3 is not installed!"; \
		echo "📥 Please install Python 3.8+ from https://python.org"; \
		exit 1; \
	fi
	@python3 --version | grep -E "Python 3\.(8|9|10|11|12|13)" >/dev/null || \
		(echo "⚠️  Python version should be 3.8 or higher" && exit 1)
	@echo "✅ Python is installed and compatible"

check-docker:
	@echo "🐳 Checking Docker installation..."
	@if ! command -v docker >/dev/null 2>&1; then \
		echo "❌ Docker is not installed!"; \
		echo "📥 Please install Docker from https://docker.com/get-started"; \
		echo "   macOS: brew install --cask docker"; \
		echo "   Ubuntu: curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh"; \
		exit 1; \
	fi
	@if ! command -v docker-compose >/dev/null 2>&1; then \
		echo "❌ Docker Compose is not installed!"; \
		echo "📥 Please install Docker Compose from https://docs.docker.com/compose/install/"; \
		exit 1; \
	fi
	@echo "✅ Docker and Docker Compose are installed"

check-env:
	@echo "🔑 Checking environment setup..."
	@if [ ! -f .env ]; then \
		echo "⚠️  .env file not found!"; \
		echo "📝 Run 'make setup-env' to create it from template"; \
		exit 1; \
	fi
	@if ! grep -q "OPENAI_API_KEY=" .env || grep -q "OPENAI_API_KEY=your_openai_api_key_here" .env; then \
		echo "⚠️  OPENAI_API_KEY not properly configured in .env"; \
		echo "📝 Please edit .env file and set your OpenAI API key"; \
		exit 1; \
	fi
	@echo "✅ Environment variables are configured"

# Installation
install: check-deps
	@echo "📦 Installing Python dependencies..."
	pip3 install -r requirements.txt
	@echo "✅ Installation completed!"

# Environment setup
setup-env:
	@echo "🔧 Setting up environment file..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "✅ Created .env file from template"; \
		echo "📝 Please edit .env file and set your OpenAI API key"; \
	else \
		echo "⚠️  .env file already exists"; \
	fi

# Testing
test: check-env
	@echo "🧪 Running tests..."
	python3 test_app.py

# Development mode (local Python)
dev: check-env install
	@echo "🚀 Starting DebateBot in development mode..."
	@echo "🌐 App will be available at http://localhost:8501"
	python3 start.py

# Docker operations
build:
	@echo "🔨 Building Docker images..."
	docker-compose build

run: check-deps setup-env
	@echo "🚀 Starting DebateBot with Docker Compose..."
	@echo "🌐 App will be available at http://localhost:8501"
	docker-compose up -d
	@echo "✅ Services started! Check logs with 'make logs'"

logs:
	@echo "📋 Showing service logs..."
	docker-compose logs -f

down:
	@echo "🛑 Stopping all services..."
	docker-compose down
	@echo "✅ All services stopped"

clean: down
	@echo "🧹 Cleaning up containers and volumes..."
	docker-compose down -v --remove-orphans
	docker system prune -f
	@echo "✅ Cleanup completed"

# Code quality
lint:
	@echo "🔍 Running code linting..."
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 . --exclude=venv,__pycache__; \
	else \
		echo "⚠️  flake8 not installed. Install with: pip install flake8"; \
	fi

format:
	@echo "🎨 Formatting code..."
	@if command -v black >/dev/null 2>&1; then \
		black . --exclude=venv; \
	else \
		echo "⚠️  black not installed. Install with: pip install black"; \
	fi

# Quick start for new users
quickstart: install setup-env
	@echo "🎉 Quick start completed!"
	@echo ""
	@echo "📝 Next steps:"
	@echo "1. Edit .env file and set your OPENAI_API_KEY"
	@echo "2. Run 'make dev' for local development"
	@echo "3. Or run 'make run' for Docker deployment"
	@echo ""
	@echo "🌐 App will be available at http://localhost:8501"
