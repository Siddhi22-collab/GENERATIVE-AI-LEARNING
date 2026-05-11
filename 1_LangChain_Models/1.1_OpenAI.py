from openai import OpenAI
client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about the  recursion in programming.",    
        }
    ],
)   
print(completion.choices[0].message.content)