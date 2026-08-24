from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    huggingfacehub_api_token=getenv("HUGGINGFACE_API_KEY"),
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Explain what an robot is in simple terms.")

print(response.content)