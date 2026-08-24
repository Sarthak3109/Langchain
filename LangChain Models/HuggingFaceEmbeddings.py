from langchain_huggingface import HuggingFaceEmbeddings

# Load an open-source embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Generate embedding
text = "LangChain is used to build LLM applications."

vector = embeddings.embed_query(text)

print("Vector size:", len(vector))
print("First 10 values:", vector[:10])