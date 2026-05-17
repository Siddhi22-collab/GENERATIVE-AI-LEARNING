from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="distilgpt2"
)

result = pipe(
    "Tell me about LangChain",
    max_new_tokens=50
)

print(result[0]["generated_text"])