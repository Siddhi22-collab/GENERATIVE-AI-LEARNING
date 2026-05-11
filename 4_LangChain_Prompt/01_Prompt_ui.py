from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Streamlit UI
st.header("Research Tool")

user_input = st.text_input("Enter your research question:")

# Create OpenAI model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

if st.button("Submit"):
    if user_input:
        response = llm.invoke(user_input)

        st.write("Response:")
        st.write(response.content)

    else:
        st.warning("Please enter a research question.")
