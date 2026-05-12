from dotenv import load_dotenv
import streamlit as st

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import load_prompt

load_dotenv()

# Load Llama model
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=200,
        temperature=0.5
    )
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper",
    ["word2vec", "bert", "diffusion models"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner Friendly", "Technical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1 paragraph)", "Medium (3-5 paragraphs)"]
)

# Load prompt template
template = load_prompt('template.json')

prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

# Button
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)