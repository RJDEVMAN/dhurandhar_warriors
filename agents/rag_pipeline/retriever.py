from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = vectordb.as_retriever(
    search_kwargs={"k":4}
)
def retrieve_context(query):

    docs = retriever.invoke(query)

    context = ""

    for doc in docs:

        context += doc.page_content

        context += "\n\n"

    return context
print("Retriever initialized successfully")