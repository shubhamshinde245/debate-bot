# --- streamlit_app.py ---
import streamlit as st
import requests
import time

# Page configuration
st.set_page_config(
    page_title="🤖 DebateBot Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for amazing UI
st.markdown(
    """
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        padding-top: 2rem;
    }
    
    /* Header Styles */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .main-header h1 {
        color: white;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        font-family: 'Inter', sans-serif;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
    }
    
    /* Card Styles */
    .debate-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border: 1px solid #e0e0e0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    /* Welcome Card Styles */
    .welcome-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.3);
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .welcome-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
    }
    
    .welcome-card h3 {
        color: white;
        margin-top: 0;
    }
    
    .welcome-card p, .welcome-card li {
        color: rgba(255,255,255,0.9);
    }
    
    .welcome-card strong {
        color: white;
    }
    
    .welcome-card em {
        color: rgba(255,255,255,0.8);
    }
    
    .debate-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    /* Input Styles */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
        font-family: 'Inter', sans-serif;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Selectbox Styles */
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Message Styles */
    .message-container {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 3px 15px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px 15px 5px 15px;
        margin: 0.5rem 0;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3);
    }
    
    .bot-message {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 15px 15px 15px 5px;
        margin: 0.5rem 0;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 3px 10px rgba(240, 147, 251, 0.3);
    }
    
    /* Sidebar Styles */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    .stError {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #feca57 0%, #ff9ff3 100%);
        border-radius: 10px;
        padding: 1rem;
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* Divider */
    .stDivider {
        margin: 2rem 0;
    }
    
    /* Animation for new messages */
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .message-animation {
        animation: slideIn 0.5s ease-out;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header h1 {
            font-size: 2rem;
        }
        .debate-card {
            padding: 1rem;
        }
    }
</style>
""",
    unsafe_allow_html=True,
)

# Amazing Header
st.markdown(
    """
<div class="main-header">
    <h1>🤖 DebateBot Pro</h1>
    <p>Engage in intelligent debates with AI-powered arguments</p>
</div>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "conversation_id" not in st.session_state:
    st.session_state["conversation_id"] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar for settings and info
with st.sidebar:
    st.markdown("### ⚙️ Settings")

    # Debate settings
    st.markdown("**🎯 Debate Configuration**")
    topic = st.text_input(
        "Debate Topic:", placeholder="e.g., Climate change is real", key="topic_input"
    )
    # Map user-friendly labels to backend values
    side_options = {"Supporting (Pro)": "pro", "Opposing (Con)": "con"}

    side_label = st.selectbox(
        "Bot's Position:",
        list(side_options.keys()),
        help="Choose which side the bot will argue",
        key="side_select",
    )

    # Get the backend value
    side = side_options[side_label]

    st.markdown("---")

    # Conversation management
    st.markdown("**💬 Conversation**")
    if st.button("🔄 Start Fresh", use_container_width=True):
        st.session_state["conversation_id"] = None
        st.session_state["messages"] = []
        st.success("✨ New conversation started!")
        st.rerun()

    st.markdown("---")

    # App info
    st.markdown("**ℹ️ About DebateBot**")
    st.markdown(
        """
    DebateBot Pro uses advanced AI to engage in intelligent debates. 
    
    **Features:**
    - 🤖 AI-powered arguments
    - 🎯 Customizable topics
    - ⚖️ Choose bot's position
    - 💾 Conversation memory
    - 🎨 Beautiful interface
    """
    )

# Main content area - messages will be displayed first, then input at the bottom

# Messages display area
if "messages" in st.session_state and st.session_state["messages"]:
    st.markdown("### 💬 Debate History")

    # Create a container for messages
    messages_container = st.container()

    with messages_container:
        for i, msg in enumerate(st.session_state["messages"]):
            if msg["role"] == "user":
                st.markdown(
                    f"""
                <div class="message-animation">
                    <div class="user-message">
                        <strong>👤 You:</strong><br>
                        {msg['message']}
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                <div class="message-animation">
                    <div class="bot-message">
                        <strong>🤖 DebateBot:</strong><br>
                        {msg['message']}
                    </div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)
else:
    # Welcome message
    st.markdown(
        """
    <div class="welcome-card">
        <h3>🎯 Welcome !</h3>
        <p>Ready to engage in an intelligent debate? Here's how to get started:</p>
        <ol>
            <li><strong>Choose a topic:</strong> Enter your debate topic in the sidebar</li>
            <li><strong>Pick bot's position:</strong> Choose whether the bot argues 'pro' or 'con'</li>
            <li><strong>Start debating:</strong> Type your argument and hit send!</li>
        </ol>
        <p><em>The AI will respond with compelling arguments from its chosen position.</em></p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Message input section - now at the bottom
st.markdown("### 💬 Your Turn")

# Create columns for input and send button
col1, col2 = st.columns([10, 1])

with col1:
    user_input = st.text_input(
        "Type your argument:",
        placeholder="Enter your debate point here... (Press Enter to send)",
        key="message_input",
        label_visibility="collapsed",
    )

with col2:
    # Use custom CSS to align the button with the input
    st.markdown(
        """
        <style>
        div[data-testid="column"]:nth-child(2) button {
            vertical-align: top !important;
            margin-top: 0px !important;
            height: 40px !important;
            width: 50px !important;
            min-width: 50px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    send_button = st.button("➤", type="primary", help="Send message")

# Check if message should be sent (button click or Enter key)
message_submitted = send_button or (
    user_input and user_input != st.session_state.get("last_input", "")
)
if message_submitted and user_input:
    # Show loading spinner
    with st.spinner("🤖 AI is thinking..."):
        payload = {
            "conversation_id": st.session_state["conversation_id"],
            "message": user_input,
            "topic": topic if topic else None,
            "side": side,
        }

        try:
            response = requests.post("http://localhost:8000/chat", json=payload)
            if response.status_code == 200:
                data = response.json()
                st.session_state["conversation_id"] = data["conversation_id"]
                st.session_state["messages"] = data["message"]
                st.session_state["last_input"] = user_input
                st.rerun()
            else:
                # If conversation not found, try starting a new one
                if "Conversation not found" in str(response.text):
                    st.warning(
                        "🔄 Previous conversation expired. Starting a new one..."
                    )
                    # Clear the conversation_id and try again
                    payload["conversation_id"] = None
                    retry_response = requests.post(
                        "http://localhost:8000/chat", json=payload
                    )
                    if retry_response.status_code == 200:
                        data = retry_response.json()
                        st.session_state["conversation_id"] = data["conversation_id"]
                        st.session_state["messages"] = data["message"]
                        st.session_state["last_input"] = user_input
                        st.success("✨ New conversation started!")
                        st.rerun()
                    else:
                        st.error(
                            f"❌ Error starting new conversation: {retry_response.status_code}"
                        )
                else:
                    st.error(f"❌ Error communicating with API: {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error(
                "🔌 Cannot connect to the API server. Please make sure the FastAPI server is running on localhost:8000"
            )

st.markdown("</div>", unsafe_allow_html=True)
