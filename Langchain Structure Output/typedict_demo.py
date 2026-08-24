from typing import TypedDict, Annotated


# TypedDict describes the required keys and value types in a dictionary.
# Annotated adds extra descriptive metadata to each type annotation.
class Human(TypedDict):
    name: Annotated[str, "name of the human"]
    age: Annotated[int, "age of the human"]
    hobbies: Annotated[list[str], "list of hobbies of the human"]


# This dictionary follows the structure and types defined by Human.
HumanExample: Human = {
    "name" : "Alice",
    "age" : 30,
    "hobbies" : ["and reading", "traveling", "cooking"]
}

print(HumanExample)