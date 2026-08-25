from os import getenv

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
  # Load environment variables from .env file
prompt1: PromptTemplate = PromptTemplate(
    template="Write a detailed report of {item} in around 200 words.",
    input_variables=["item"]
)

prompt2: PromptTemplate = PromptTemplate(
    template="Write a short summary of {item} in less than 50 words.",
    input_variables=["item"]
)

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    huggingfacehub_api_token=getenv("HUGGINGFACE_API_KEY"),
    task="conversational",
)

model = ChatHuggingFace(llm=llm)

# response = model.invoke(prompt.format(item="LangChain"))


# print(response.content)


chain  = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke(prompt1.format(item="LangChain"))

print(response)

print(chain.get_graph().print_ascii())  # Visualize the chain as a graph in DOT format