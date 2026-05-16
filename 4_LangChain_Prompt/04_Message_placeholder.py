from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

history = """
User: Hi
Assistant: Hello

User: I ordered a laptop
Assistant: Please share your order ID
"""

prompt = f"""
You are a helpful customer support agent.

Chat History:
{history}

User: Where is my refund?
Assistant:
"""

result = pipe(prompt, max_new_tokens=100)

print(result[0]["generated_text"])