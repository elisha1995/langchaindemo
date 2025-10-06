import os

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

from dotenv import load_dotenv

load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["country", "no_of_paras", "language"],
    template="""You are an expert in traditional cuisines.
                You provide information about a specific dish from a specific country.
                Avoid giving information about fictional places. If the country is fictional
                or non-existent, answer: I don't know.
                Answer the question: What is the traditional cuisine of {country}?
                Answer in {no_of_paras} paragraphs in {language}.
            """
)

st.title("Cuisine Info")
country = st.text_input("Enter the country: ")
no_of_paras = st.number_input("Enter the number of paragraphs: ", min_value=1, max_value=5)
language = st.text_input("Enter the language: ")

if country:
    response = llm.invoke(prompt_template.format(country=country, no_of_paras=no_of_paras, language=language))
    st.write(response.content)
