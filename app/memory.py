import faiss
import numpy as np

dim = 1536
index = faiss.IndexFlatL2(dim)

memory_store = []

def add_memory(vector, text):
    index.add(np.array([vector]).astype("float32"))
    memory_store.append(text)

def search_memory(vector, k=3):
    D, I = index.search(np.array([vector]).astype("float32"), k)
    return [memory_store[i] for i in I[0] if i < len(memory_store)]
