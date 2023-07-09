import pandas as pd
from pdf.downloader_pdf import telechargement, get_summary
from pdf.extract_pdf import get_images, get_text
from dotenv import load_dotenv
from web.back.embedding import classic_embedding
import os
import numpy as np

if __name__ == '__main__':

    urls = pd.read_csv("data/URLs.csv").values.ravel()
    load_dotenv()
    print("Hello chat")

    for f in urls:
        #telechargement(f)
        scrapping = get_summary(f)
        if scrapping is not None:
            domain, summary = scrapping
            
            embedding = np.array(classic_embedding(summary, True))

            path = os.path.join("data", "embedding_summary", domain)
            if not os.path.exists(path):
                os.makedirs(path)
            np.save(os.path.join(path, f + ".npy"), embedding)



    #get_images("/home/virgaux/Travail/langchain/data/theses/edutice-00000207v1.pdf")
    #print(get_text("/home/virgaux/Travail/langchain/data/theses/edutice-00000207v1.pdf", 40))