from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import os

class Embedder:
    def __init__(self):
        self.model_name = 'sentence-transformers/all-MiniLM-L6-v2'

    def build_vectorstore(self, articles):
        """
        Convert the articles to Documents, generate embeddings, 
        and create a FAISS vector store to store the embeddings.
        """
        documents = [
            Document(page_content=article["content"], metadata={"title": article["title"], "url": article["url"]}) 
            for article in articles
        ]
        huggingface_embeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        vectorstore = FAISS.from_documents(documents, huggingface_embeddings)

        return vectorstore
