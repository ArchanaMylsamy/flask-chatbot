Flask Chatbot Application
=========================

A simple, lightweight chatbot built with **Python Flask** and a modern **HTML/CSS/JS** frontend.

## Features

- 🤖 Rule-based chatbot with keyword matching
- 💬 Clean, modern chat interface with real-time responses
- ⚡ Quick action buttons for common commands
- 📱 Responsive design (works on mobile)
- 🔑 No API keys required — runs locally

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/ArchanaMylsamy/flask-chatbot.git
cd flask-chatbot
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. **Open your browser** and go to `http://localhost:5000`

## What You Can Ask

Try these commands:

| Command | Example Response |
|---------|-----------------|
| `hello` | Greeting message |
| `joke` | Random programmer joke |
| `motivate` | Inspirational quote |
| `who created you` | Developer info |
| `what can you do` | Capabilities list |
| `thanks` | Friendly response |

## Project Structure

```
flask-chatbot/
├── app.py                 # Flask backend with chat logic
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── templates/
    └── index.html        # Frontend chat UI
```

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Hosting:** Local (run on your machine)

## License

MIT License — Feel free to use and modify!

---

Built with ❤️ by [ArchanaMylsamy](https://github.com/ArchanaMylsamy)