from pydantic import BaseModel, Field


# BaseModel creates a data model that validates values at runtime.
class Human(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(description="The person's age")
    hobbies: list[str] = Field(description="A list of hobbies")


# Pydantic validates this data and creates a Human object.
human_example = Human(
    name="Alice",
    age=30,
    hobbies=["reading", "traveling", "cooking"],
)

# model_dump converts the validated model into a regular dictionary.
print(human_example.model_dump())
