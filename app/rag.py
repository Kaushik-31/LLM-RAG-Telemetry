# toy retriever; replace with FAISS/Pinecone later
from random import randint

def retrieve(query: str) -> list[str]:
    # pretend we retrieved k docs
    k = randint(1, 3)
    return [f"doc_{i}_about_{query}" for i in range(k)]
