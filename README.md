# 🧠 LangGraph Multi-turn Chatbot

A sophisticated chatbot application built with Streamlit, LangGraph, and LangChain, featuring multi-turn conversation capabilities powered by Groq's LLM.

## 📋 Overview

This project implements a conversational AI chatbot with the following key features:
- Interactive web interface using Streamlit
- Multi-turn conversation support using LangGraph
- Integration with Groq's Llama3-8b model
- Persistent chat history within sessions
- Clean and intuitive user interface

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **LangGraph**: For managing conversation flow
- **LangChain**: LLM integration framework
- **Groq**: LLM provider using Llama3-8b model
- **Python**: Programming language

## 🚀 Getting Started

### Prerequisites

- Python >= 3.11
- Groq API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Groq API key:
