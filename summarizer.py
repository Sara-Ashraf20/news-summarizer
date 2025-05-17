from langchain.chains import AnalyzeDocumentChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains.summarize import load_summarize_chain

class Summarizer:
    def __init__(self):
        self.llm = OpenAI(temperature=0)
        self.map_reduce_chain = load_summarize_chain(self.llm, chain_type="map_reduce")
        self.summarize_chain = load_summarize_chain(self.llm, chain_type="stuff")

    def summarize(self, documents, mode="brief"):
        if mode == "brief":
            summary = self.summarize_chain.invoke(documents)  
        else:
            summary = self.map_reduce_chain.invoke(documents)  
        return summary
