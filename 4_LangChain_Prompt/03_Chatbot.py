from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100
)

messages = [
    {"role": "system", "content": "You are a helpful cricket expert"},
    {"role": "user", "content": "Explain in simple terms, what is Dusra"}
]

result = pipe(messages)

print(result[0]["generated_text"])