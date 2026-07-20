"""Flask Chatbot Application."""

import random
import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple rule-based responses for the chatbot
RESPONSES = {
    "greeting": [
        "Hello! 👋 How can I help you today?",
        "Hi there! Welcome! What can I do for you?",
        "Hey! Great to see you. What's on your mind?",
    ],
    "goodbye": [
        "Goodbye! Have a great day! 👋",
        "See you later! Feel free to come back anytime.",
        "Bye! It was nice chatting with you! 😊",
    ],
    "help": [
        "I can help with general questions. Try asking me about:\n"
        "- Who made me? (ask 'who created you')\n"
        "- What can I do? (ask 'what can you do')\n"
        "- Jokes, motivation, or just chat!\n"
        "Type 'help' anytime for this list.",
    ],
    "creator": [
        "I was created by ArchanaMylsamy, a Software Development Engineer! 🚀",
        "My developer is Archana — an SDE with a passion for full-stack development.",
    ],
    "capabilities": [
        "I'm a rule-based chatbot. I can chat, tell jokes, share motivation, and more! 🤖",
        "I respond to keywords and patterns. Try saying 'hello', 'joke', 'motivate', or 'help'!",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
        "Why did the developer go broke? Because he used up all his cache! 💸",
        "What's a programmer's favorite hangout? Foo Bar! 🍺",
        "Why do Java developers wear glasses? Because they can't C#! 👓",
        "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡",
    ],
    "motivation": [
        "The only way to do great work is to love what you do. — Steve Jobs 💪",
        "Code is like humor. When you have to explain it, it's bad. — Cory House ✨",
        "First, solve the problem. Then, write the code. — John Johnson 🧠",
        "The expert in anything was once a beginner. — Helen Hayes 🌟",
        "It does not matter how slowly you go as long as you do not stop. — Confucius 🏃",
    ],
    "thanks": [
        "You're welcome! Happy to help! 😊",
        "Glad I could help! Anything else?",
        "No problem! That's what I'm here for! 🙌",
    ],
    "name": [
        "I'm FlaskBot — a simple chatbot built with Python and Flask! 🤖",
        "You can call me FlaskBot. I'm lightweight but friendly!",
    ],
    "weather": [
        "I can't check real-time weather yet, but I hope it's sunny where you are! ☀️ Try checking weather.com for live updates.",
    ],
    "time": [
        "I don't have access to real-time clocks, but check your system clock! ⏰",
    ],
    "love": [
        "Love is the most powerful algorithm — it optimizes every heart! ❤️",
        "They say love is complex, but its code has no bugs. 💕",
    ],
    "food": [
        "I may be a chatbot, but I love talking about food! 🍕 What's your favorite cuisine?",
        "If I could eat, I'd probably enjoy some good Python... just kidding! 😄 What's your favorite food?",
    ],
    "music": [
        "I can't hear music, but I know programmers love both lo-fi beats and silence while coding! 🎵",
    ],
    "python": [
        "Python is amazing! Simple, readable, and powerful. The best language for beginners and pros alike! 🐍",
        "Python: 'Readability counts' — that's why it's the #1 language for AI and web development!",
    ],
    "programming": [
        "Programming is the art of telling another human what one wants the computer to do. 🖥️",
        "The best programmers code not just for machines, but for other humans. 👨‍💻",
    ],
}

# Default fallback responses
DEFAULT_RESPONSES = [
    "Hmm, I'm not sure I understand. Try asking me for a 'joke', 'motivation', or type 'help'! 😊",
    "That's interesting! I'm a simple bot — try 'help' to see what I can do.",
    "I didn't quite catch that. Type 'help' for a list of things I can respond to!",
    "Could you rephrase that? I work best with keywords like 'hello', 'joke', or 'motivate'! 🤔",
    "Let me think about that... I'm still learning! Try 'help' for what I know. 😄",
]


def find_best_response(message):
    """Analyze the message and return the best matching response."""
    msg = message.lower().strip()

    # Remove common punctuation for better matching
    msg_clean = re.sub(r"[^\w\s]", "", msg)
    words = set(msg_clean.split())

    # Pattern matching for each category
    patterns = {
        "greeting": ["hello", "hi", "hey", "greetings", "howdy", "sup", "what's up"],
        "goodbye": ["bye", "goodbye", "see you", "later", "take care", "cya"],
        "help": ["help", "what can you do", "commands", "options", "guide"],
        "creator": ["who created", "who made", "developer", "creator", "archana"],
        "capabilities": ["what can you do", "your capabilities", "features", "what are you"],
        "joke": ["joke", "funny", "humor", "laugh", "make me laugh"],
        "motivation": ["motivat", "inspire", "inspir", "encourage", "quote", "sayings"],
        "thanks": ["thank", "thanks", "appreciate", "grateful", "thx"],
        "name": ["your name", "who are you", "what are you", "call you", "name"],
        "weather": ["weather", "temperature", "rain", "sunny", "forecast"],
        "time": ["time", "clock", "what time", "current time"],
        "love": ["love", "romance", "crush", "relationship"],
        "food": ["food", "eat", "hungry", "restaurant", "cook", "recipe", "cuisine"],
        "music": ["music", "song", "playlist", "band", "sing"],
        "python": ["python", "programming language"],
        "programming": ["programming", "coding", "code", "developer", "software"],
    }

    for category, keywords in patterns.items():
        for keyword in keywords:
            if keyword in msg or keyword in msg_clean:
                return random.choice(RESPONSES[category])

    # Check for question patterns
    if "?" in message:
        return "That's a great question! I'm a simple bot — try 'help' to see what I can do. 🤔"

    # Default fallback
    return random.choice(DEFAULT_RESPONSES)


@app.route("/")
def index():
    """Serve the chat interface."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    """Handle chat messages and return bot responses."""
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "Please type a message! 💬"}), 200

    # Get the best response
    bot_response = find_best_response(user_message)

    return jsonify({"response": bot_response})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)