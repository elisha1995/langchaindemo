import os

from langchain_openai import ChatOpenAI
import streamlit as st

from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

st.title("Question Answering App")
question = st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)
