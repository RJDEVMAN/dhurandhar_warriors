from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from loader import load_documents
documents = load_documents()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(

    documents=chunks,

    embedding=embeddings,

    persist_directory="chroma_db"

)

print("Knowledge Base Created")