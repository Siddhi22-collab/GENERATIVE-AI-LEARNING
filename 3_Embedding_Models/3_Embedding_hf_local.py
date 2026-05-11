from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2", dimensions=384)
text = "What is the capital of France?"
vector = embedding.embed_query(text)
print(vector)