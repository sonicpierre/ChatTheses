from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
import pinecone
import numpy as np
from embedding import classic_embedding
from dotenv import load_dotenv
import os


FOLDER_SUMMARY = r"/home/virgaux/Travail/langchain/data/summary"

def find_files(filename, search_path):
   result = []

    # Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result


def get_documents(user_question):
   
    emb = classic_embedding(user_question, prod=True)

    query = index.query(
        vector=list(emb.astype(np.float64)),
        top_k=3,
        include_values=True
        )
   
    txt_files = []
    for i in range(3):
        name_these = query['matches'][i]['id']
        search_path = find_files(name_these + ".txt", FOLDER_SUMMARY)

        if len(search_path)>0:
            with open(search_path[0], "r") as f:
                txt_files.append("".join(f.readlines()))

        else:
            print("File not found")

    return "\n \n".join(txt_files)


if __name__ == '__main__':

    load_dotenv()

    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="asia-southeast1-gcp-free")
    index = pinecone.Index("thesesv2")
    embedding = OpenAIEmbeddings()

    c = input("Enter your question : \n")

    doc_txt = get_documents(c)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.create_documents(doc_txt)

    docsearch = FAISS.from_documents(docs, embedding)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), docsearch.as_retriever(), memory=memory)

    chat_history = []
    while c!= "exit":
        retriever = docsearch.as_retriever(search_type="mmr")
        result = qa({"question": c, "chat_history": chat_history})
        print(result['answer'])

        c = input()
