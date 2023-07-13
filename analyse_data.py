import os
import numpy as np
import glob

EMBBEDDED_MODEL_OUTPUT = 1536
MAIN_FOLDER = "data/embedding_summary"

if __name__ == '__main__':

    li_domains = os.listdir(MAIN_FOLDER)
    dict_embedding = {}

    for t in range(len(li_domains)):
        arrays = glob.glob(os.path.join(MAIN_FOLDER, li_domains[t], "*.npy"))
        for arr in arrays:
            if li_domains[t] not in dict_embedding:
                dict_embedding[li_domains[t]] = []
                
            dict_embedding[li_domains[t]].append(np.load(arr))

    print(dict_embedding)