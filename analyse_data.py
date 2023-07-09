import os
import numpy as np

EMBBEDDED_MODEL_OUTPUT = 1536
FOLDER = "data/embedding_summary"

if __name__ == '__main__':

    li_tables = os.listdir(FOLDER)
    arr_embedded = np.zeros((len(li_tables), EMBBEDDED_MODEL_OUTPUT))

    for t in range(len(li_tables)):
        arr_embedded[t] = np.load(os.path.join(FOLDER, li_tables[t]))

    print(arr_embedded.shape)