from langchain_google_genai import chat_google_genai
from docenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.9)
result=model.invoke("What is the capital of France?")
print(result.content)