from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)
document = ["Paris is the capital of France.",
"lomdon is the capital of UK.",
"Berlin is the capital of Germany."]

rsult=embedding.embed_documents(document)
print(rsult)