import pinecone
from dotenv import load_dotenv
import os
import numpy as np
from web.back.embedding import classic_embedding

FOLDER_SUMMARY = r"data/summary"

def find_files(filename, search_path):
   result = []

    # Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

if __name__ == '__main__':

    load_dotenv()

    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="asia-southeast1-gcp-free")

    index = pinecone.Index("theses")
    
    user_question = "Quelle fonction mathématiques peut approximer cosinus ?"

    emb = classic_embedding(user_question, prod=True)

    query = index.query(
        vector=list(emb.astype(np.float64)),
        top_k=3,
        include_values=True
        )
    
    name_these = query['matches'][0]['id']
    search_path = find_files(name_these + ".txt", FOLDER_SUMMARY)

    if len(search_path)>0:
       with open(search_path[0], "r") as f:
          print("".join(f.readlines()))

    else:
       print("File not found")
