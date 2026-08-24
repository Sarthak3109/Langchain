# LangChain Models

This folder contains a few simple examples showing how to use LangChain with open-source and Hugging Face models.

The goal is to help you understand the difference between:
- text generation models
- chat models
- embedding models

## Files in this folder

### 1. ChatGPTModel.py
This example uses a Hugging Face-hosted model through `HuggingFaceEndpoint` and `ChatHuggingFace`.

It demonstrates:
- loading a model endpoint
- sending a prompt as a chat message
- printing the model response

This example requires a Hugging Face token in a `.env` file:

```env
HUGGINGFACE_API_KEY=your_token_here
```

### 2. HuggingFaceModel.py
This example uses `HuggingFacePipeline` with an open-source model from Hugging Face.

It demonstrates:
- loading a text-generation pipeline
- generating text from a prompt
- using a local or downloaded model without a direct API key

This is a good example for experimenting with open-source LLMs.

### 3. HuggingFaceEmbeddings.py
This example uses `HuggingFaceEmbeddings`.

It demonstrates:
- converting text to vectors
- creating semantic representations of input text
- measuring vector length for downstream tasks like search and retrieval

Embeddings are especially useful for:
- semantic search
- RAG systems
- document similarity
- recommendation-style matching

## Prerequisites

Install the required packages in your virtual environment:

```bash
pip install langchain langchain-huggingface transformers python-dotenv
```

## Common concepts

### LLM
A large language model generates text from a prompt.

### Chat model
A chat model is designed for conversation and works with system/user/assistant messages.

### Embedding model
An embedding model converts text into vectors so similar text can be compared numerically.

## Typical workflow

1. Choose a model or provider
2. Send a prompt or message
3. Handle the model output
4. Use the output for app logic, search, or chat experiences

## Example usage

```python
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tokenizer="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=120,
)

llm = HuggingFacePipeline(pipeline=pipe)
print(llm.invoke("Explain LangChain in one sentence."))
```

## Notes

- Model downloads may take time the first time they are used.
- Some models require a token or internet access.
- Open-source models are a good option for local experimentation and learning.

## Summary

This folder is a beginner-friendly introduction to:
- Hugging Face models in LangChain
- chat-style model prompting
- embedding generation for semantic tasks
