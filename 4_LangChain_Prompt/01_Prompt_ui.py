from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st

# Streamlit UI
st.header("Research Tool")

user_input = st.text_input("Enter your research question:")

# Hugging Face local model
llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100
    }
)

model = ChatHuggingFace(llm=llm)

# Button click
if st.button("Submit"):

    if user_input:

        response = model.invoke(user_input)

        st.write("Response:")
        st.write(response.content)

    else:
        st.warning("Please enter a research question.")