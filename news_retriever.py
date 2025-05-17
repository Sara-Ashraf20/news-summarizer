import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=api_key)

def get_articles(topic, page_size=10):
    """Fetch articles based on a topic using NewsAPI."""
    try:
        response = newsapi.get_everything(
            q=topic,
            language='en',
            sort_by='relevancy',
            page_size=page_size
        )

        if response["status"] != "ok":
            print("Error: Unable to fetch news articles.")
            return []

        articles = []
        for article in response["articles"]:
            if article.get("content"): 
                articles.append({
                    "title": article["title"],
                    "content": article["content"],
                    "url": article["url"]
                })
        return articles
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    topic = input("Enter a topic to search for news: ")
    news = get_articles(topic)
    if news:
        for i, article in enumerate(news):
            print(f"\n{i+1}. {article['title']}")
            print(article['url'])
    else:
        print("No articles found.")
