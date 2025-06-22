from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import shutil
import os


load_dotenv()

DATA = 'the_death_of_vivek_oji.pdf'


def load_docs():
    loader = PDFMinerLoader(DATA)
    documents = loader.load()
    return documents


documents = load_docs()


text_splitter  = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100,
    length_function = len,
    add_start_index = True)

chunks = text_splitter.split_documents(documents)

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

DB = './db'

REBUILD_DB = True

if REBUILD_DB:
    if os.path.exists(DB):
        shutil.rmtree(DB) 
    print("Creating new vectorstore and embedding documents")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB
    )
else:
    print('Loading existing Chroma Vector Store...')
    vectorstore = Chroma(
        persist_directory=DB,
        embedding_function=embedding
    )


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.3
)



retriever = vectorstore.as_retriever(
    search_type="mmr",              
    search_kwargs={
        "k": 5,                      
        "lambda_mult": 0.5           
    }
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever= retriever,
    return_source_documents=True,
    chain_type="stuff",
)



while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        break

    result = qa_chain.invoke({"query": query})
   
    print("\n🤖 Answer:\n", result['result'])

    print("\n📚 Source Chunks:")
    for i, doc in enumerate(result['source_documents'], 1):
        print(f"\n--- Chunk {i} ---\n{doc.page_content}")
