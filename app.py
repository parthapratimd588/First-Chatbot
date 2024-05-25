from langchain_groq import ChatGroq
import streamlit as st

GROQ_API_KEY = str("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")

llm = ChatGroq(groq_api_key = GROQ_API_KEY,
               model_name = "llama3-70b-8192")

query = st.text_input("Enter query here")

if query:
    with st.spinner(":green[processig . . .]"):
        response = llm.invoke(query).content
        st.success(response)
        st.info(response)
        st.warning(response)

