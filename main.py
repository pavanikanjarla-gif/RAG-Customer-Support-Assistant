from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

# -----------------------------
# LOAD PDF
# -----------------------------
loader = PyPDFLoader("data.pdf")
documents = loader.load()

# -----------------------------
# SPLIT
# -----------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(documents)

# -----------------------------
# EMBEDDINGS + VECTOR DB
# -----------------------------
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="db"
)

retriever = vectorstore.as_retriever()

# -----------------------------
# GROQ LLM
# -----------------------------
llm = ChatGroq(model="llama-3.1-8b-instant")

# -----------------------------
# ASK QUESTION
# -----------------------------
query = input("Ask a question: ")

docs = retriever.invoke(query)

if not docs:
    print("❌ No relevant documents found")
else:
    context = docs[0].page_content

    response = llm.invoke(f"""
    Answer based only on the context below.

    Context:
    {context}

    Question:
    {query}
    """)

    print("\n🤖 AI Answer:\n")
    print(response.content)