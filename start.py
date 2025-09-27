#!/usr/bin/env python3
"""
Startup script for DebateBot
This script starts the Streamlit app with integrated AI functionality
"""

import sys
import subprocess
import argparse


def start_streamlit():
    """Start the Streamlit app"""
    print("🚀 Starting DebateBot Pro on http://localhost:8501")
    print("🤖 Using integrated AI processing")
    subprocess.run(["streamlit", "run", "streamlit_app.py"])


def main():
    parser = argparse.ArgumentParser(description="DebateBot Startup Script")
    parser.add_argument(
        "--help-setup",
        action="store_true",
        help="Show setup instructions",
    )

    args = parser.parse_args()

    if args.help_setup:
        print("🚀 DebateBot Pro Setup Instructions")
        print("=" * 50)
        print("1. Install dependencies:")
        print("   pip install -r requirements.txt")
        print()
        print("2. Set up your OpenAI API key:")
        print("   Create a .env file with: OPENAI_API_KEY=your_key_here")
        print()
        print("3. Run the app:")
        print("   python start.py")
        print("   or")
        print("   streamlit run streamlit_app.py")
        print()
        print("4. For Streamlit Cloud deployment:")
        print("   - Push code to GitHub")
        print("   - Deploy on Streamlit Cloud")
        print("   - Add OPENAI_API_KEY as a secret")
        return

    start_streamlit()


if __name__ == "__main__":
    main()
