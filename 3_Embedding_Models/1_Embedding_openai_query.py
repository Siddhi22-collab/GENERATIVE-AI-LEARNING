from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
embedding=OpenAIEmbeddings(model="text-embedding-3-small", dimensions=1024)
rsult=embedding.embed_query("What is the capital of France?")
print(rsult)