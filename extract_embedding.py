import pandas as pd
from pdf.downloader_pdf import telechargement, get_summary
from pdf.extract_pdf import get_images, get_text
from dotenv import load_dotenv
from web.back.embedding import classic_embedding
import os
import numpy as np
import pinecone


if __name__ == '__main__':

    load_dotenv()
    urls = pd.read_csv("data/URLs.csv").values.ravel()

    #Allow storing summary in pinecone
    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="asia-southeast1-gcp-free")
    index = pinecone.Index("theses")
    
    print("Start extraction of summaries !!")

    for f in urls:
        print(f)

        #telechargement(f)
        scrapping = get_summary(f)
        if scrapping is not None:
            domain, summary = scrapping
            
            embedding = np.array(classic_embedding(summary, True))

            path = os.path.join("data", "embedding_summary", domain)
            if not os.path.exists(path):
                os.makedirs(path)
            
            np.save(os.path.join(path, f + ".npy"), embedding)
            index.upsert([
                (f, list(embedding.astype(np.float64)), {"domain": domain})
            ])



    #get_images("/home/virgaux/Travail/langchain/data/theses/edutice-00000207v1.pdf")
    #print(get_text("/home/virgaux/Travail/langchain/data/theses/edutice-00000207v1.pdf", 40))