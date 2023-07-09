from langchain.embeddings import FakeEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
import numpy as np
import tiktoken

FIRST_MODEL = "text-embedding-ada-002" #8191 as input, 1536 in output
SECOND_MODEL = "cl100k_base"

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""

    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))

    return num_tokens

def classic_embedding(txt:str, prod = False):
    
    if prod:
        embeddings = OpenAIEmbeddings(model=FIRST_MODEL, tiktoken_model_name=SECOND_MODEL)
    else:
        embeddings = FakeEmbeddings(size=1000)

    nb_token = num_tokens_from_string(txt, SECOND_MODEL)
    print("Number of input tokens", nb_token)

    query_result = embeddings.embed_query(txt)
    
    return np.array(query_result, dtype=np.float32)

