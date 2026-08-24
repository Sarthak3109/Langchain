from os import getenv
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


class Recipe(TypedDict):
    name: Annotated[str, "The recipe name"]
    ingredients: Annotated[list[str], "The recipe ingredients"]
    preparation_time_minutes: Annotated[
        int, "The estimated preparation time in minutes"
    ]


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    huggingfacehub_api_token=getenv("HUGGINGFACE_API_KEY"),
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)
structured_chat = chat.with_structured_output(Recipe)
recipe: Recipe = structured_chat.invoke(
    "Generate a simple vegetarian recipe for pasta primavera."
)

print(recipe)
