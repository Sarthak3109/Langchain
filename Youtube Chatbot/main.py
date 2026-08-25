from os import getenv

from dotenv import load_dotenv
from langchain_community.document_loaders import YoutubeLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

video_url = getenv("YOUTUBE_URL")
if not video_url:
	raise ValueError("Set YOUTUBE_URL to the YouTube video URL before running this script.")

documents = YoutubeLoader.from_youtube_url(
	video_url,
	add_video_info=False,
).load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
	model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_store = InMemoryVectorStore.from_documents(chunks, embedding=embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 6})

llm = HuggingFaceEndpoint(
	repo_id="openai/gpt-oss-120b",
	huggingfacehub_api_token=getenv("HUGGINGFACE_API_KEY"),
	task="conversational",
)
chat = ChatHuggingFace(llm=llm)

prompt = ChatPromptTemplate.from_template(
	"""Summarize the YouTube video using only the transcript context below.
Include the main topic, the most important points, and the final takeaway.
If the context is insufficient, say so instead of inventing information.

Transcript context:
{context}
"""
)

retrieved_documents = retriever.invoke("What are the main ideas and key takeaways?")
context = "\n\n".join(document.page_content for document in retrieved_documents)
response = chat.invoke(prompt.format_messages(context=context))

print(response.content)
