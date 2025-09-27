#!/usr/bin/env python3
"""
Startup script for DebateBot
This script can start either the FastAPI server or the Streamlit app
"""

import sys
import subprocess
import argparse


def start_api_server():
    """Start the FastAPI server"""
    print("🚀 Starting FastAPI server on http://localhost:8000")
    subprocess.run([sys.executable, "api_server.py"])


def start_streamlit():
    """Start the Streamlit app"""
    print("🚀 Starting Streamlit app on http://localhost:8501")
    subprocess.run(["streamlit", "run", "streamlit_app.py"])


def main():
    parser = argparse.ArgumentParser(description="DebateBot Startup Script")
    parser.add_argument(
        "mode",
        choices=["api", "streamlit", "both"],
        help="Choose what to start: api, streamlit, or both",
    )

    args = parser.parse_args()

    if args.mode == "api":
        start_api_server()
    elif args.mode == "streamlit":
        start_streamlit()
    elif args.mode == "both":
        print("🚀 Starting both FastAPI server and Streamlit app")
        print("📝 Note: Start them in separate terminals for best experience")
        print("\n1. First terminal: python start.py api")
        print("2. Second terminal: python start.py streamlit")
        print(
            "\nOr use the integrated mode by just running: streamlit run streamlit_app.py"
        )


if __name__ == "__main__":
    main()
