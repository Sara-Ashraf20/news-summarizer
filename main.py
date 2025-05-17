from embedding_engine import Embedder 
from summarizer import Summarizer
from news_retriever import get_articles 
from user_manager import UserManager
from langchain.schema import Document  

def main():
    embedder = Embedder()
    summarizer = Summarizer()  
    user_manager = UserManager()  

    while True:
        print("\n1. Search News by Topic")
        print("2. View Saved Topics")
        print("3. View Search History")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            topic = input("Enter topic: ")
            summary_type = input("Summary type (brief/detailed): ").lower()
            
            articles = get_articles(topic)  
            if articles:
                documents = [
                    Document(page_content=article["content"], metadata={"title": article["title"], "url": article["url"]}) 
                    for article in articles
                ]

                # Summarize the news articles
                summary = summarizer.summarize(documents, mode=summary_type)
                print(f"Summary:\n{summary}")

                # Save to user history
                user_manager.log_search(topic)

        elif choice == "2":
            # View saved topics
            saved_topics = user_manager.get_preferences()
            if saved_topics:
                print("Saved Topics:")
                for topic in saved_topics:
                    print(topic)
            else:
                print("No saved topics.")

        elif choice == "3":
            # View search history
            search_history = user_manager.get_history()
            if search_history:
                print("Search History:")
                for record in search_history:
                    print(f"Topic: {record}")
            else:
                print("No search history.")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
