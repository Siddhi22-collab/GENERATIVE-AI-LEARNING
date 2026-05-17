from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from typing import TypedDict
from transformers import pipeline

load_dotenv()

# Hugging Face pipeline
pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100
)

# Convert pipeline into LangChain model
llm = HuggingFacePipeline(pipeline=pipe)

# Chat model
model = ChatHuggingFace(llm=llm)

# Structured output schema
class Review(TypedDict):
    summary: str
    sentiment: str

# Structured output
structured_model = model.with_structured_output(Review)

# Invoke
result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!

The camera quality is amazing and battery lasts all day.

However, the phone feels heavy for one-handed use.
""")

print(result)