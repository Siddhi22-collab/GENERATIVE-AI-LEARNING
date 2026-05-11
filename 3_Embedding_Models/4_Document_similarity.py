from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)
document = ["Paris is the capital of France.",
"lomdon is the capital of UK.",
"Berlin is the capital of Germany."]
query = "What is the capital of France?"
document_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)
print(cosine_similarity([query_embedding], document_embeddings))