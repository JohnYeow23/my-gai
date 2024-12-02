import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

class ModelSelector:
    def __init__(self, openai_api_key):
        self.api_key = openai_api_key

    def get_chat_model(self, model_name="gpt-4o", temperature=0):
        return ChatOpenAI(
            model=model_name,
            api_key=self.api_key,
            temperature=temperature,
        )

    def get_embedding_model(self, embedding_model="text-embedding-ada-002"):
        return OpenAIEmbeddings(
            model=embedding_model,
            openai_api_key=self.api_key,
        )

    def get_tracing_settings(self):
        return {
            "tracing_v2": os.getenv("LANGCHAIN_TRACING_V2"),
            "langsmith_api_key": os.getenv("LANGCHAIN_API_KEY"),
        }
