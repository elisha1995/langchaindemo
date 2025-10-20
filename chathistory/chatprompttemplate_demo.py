import os
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a Agile Coach. Answer any questions "
                  "related to the agile process"),
        ("human", "{input}")
    ]
)

st.title("Agile Guide")

text_input = st.text_input("Enter the question:")

chain = prompt_template | llm

if text_input:
    response = chain.invoke({"input":text_input})
    st.write(response.content)