#!/usr/bin/env python3
"""
Test script for DebateBot functionality
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def test_imports():
    """Test that all modules can be imported"""
    print("🧪 Testing imports...")

    try:
        import streamlit_app

        print("✅ streamlit_app imports successfully")
    except Exception as e:
        print(f"❌ streamlit_app import failed: {e}")
        return False

    try:
        import api_server

        print("✅ api_server imports successfully")
    except Exception as e:
        print(f"❌ api_server import failed: {e}")
        return False

    try:
        from task_2.models import ChatRequest, Message, ChatResponse

        print("✅ Models import successfully")
    except Exception as e:
        print(f"❌ Models import failed: {e}")
        return False

    try:
        from task_2.prompt import SYSTEM_PROMPT

        print("✅ Prompt imports successfully")
    except Exception as e:
        print(f"❌ Prompt import failed: {e}")
        return False

    return True


def test_environment():
    """Test environment setup"""
    print("\n🧪 Testing environment...")

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("✅ OPENAI_API_KEY is set")
        return True
    else:
        print("⚠️  OPENAI_API_KEY is not set (required for AI functionality)")
        print("   Create a .env file with: OPENAI_API_KEY=your_key_here")
        return False


def test_models():
    """Test Pydantic models"""
    print("\n🧪 Testing models...")

    try:
        from task_2.models import ChatRequest, Message, ChatResponse

        # Test Message model
        msg = Message(role="user", message="Hello")
        print(f"✅ Message model works: {msg}")

        # Test ChatRequest model
        req = ChatRequest(message="Hello", topic="AI", side="pro")
        print(f"✅ ChatRequest model works: {req}")

        # Test ChatResponse model
        resp = ChatResponse(conversation_id="test", message=[msg])
        print(f"✅ ChatResponse model works: {resp}")

        return True
    except Exception as e:
        print(f"❌ Model test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 DebateBot Test Suite")
    print("=" * 50)

    tests = [
        test_imports,
        test_environment,
        test_models,
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")

    if passed == total:
        print("🎉 All tests passed! Your DebateBot is ready to go!")
        print("\n🚀 Next steps:")
        print("1. Set your OPENAI_API_KEY in .env file")
        print("2. Run: streamlit run streamlit_app.py")
        print("3. Or run: python start.py streamlit")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
