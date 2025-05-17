<<<<<<< HEAD
📰 AI News Summarizer

This is a CLI-based Python project that retrieves news articles on a given topic using NewsAPI, summarizes them using OpenAI (via LangChain), and logs your search history and preferences.

---

🚀 Features

- Fetches news using NewsAPI.
- Summarizes news using OpenAI LLMs (brief/detailed).
- Saves your search history and preferred topics locally.
- Vectorizes articles using HuggingFace + FAISS.


----
How to Run
1. Install dependencies
pip install -r requirements.txt
2. Set up environment variables
Create a .env file in the project root with the following content:
NEWS_API_KEY=your_news_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
3. Run the app
python main.py
