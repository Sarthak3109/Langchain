from os import getenv

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from pydantic import BaseModel, Field


# BaseModel defines the schema and validates the model's structured response.
class Recipe(BaseModel):
    name: str = Field(description="The recipe name")
    ingredients: list[str] = Field(description="The recipe ingredients")
    preparation_time_minutes: int = Field(
        description="The estimated preparation time in minutes"
    )


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

# model_dump converts the validated Pydantic object into a dictionary.
print(recipe.model_dump())
