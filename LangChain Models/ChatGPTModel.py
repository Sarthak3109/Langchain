from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

response = llm.invoke("Write a short summary of LangChain.")
print(response)