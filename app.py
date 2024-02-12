import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe

# Open AI API Key
load_dotenv()

openai_api_key = os.getenv("OPENAI_KEY")


# Function for pandas ai to query CSV File
def chat_with_csv(df, prompt):
    llm = OpenAI(api_token=openai_api_key)
    df = SmartDataframe(df, config={"llm": llm})
    result = df.chat(prompt)
    return result


st.set_page_config(layout="wide")

st.title("Finance AI")

input_csv = st.file_uploader("Upload your CSV File", type=["csv", "xlsx"])

if input_csv is not None:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("CSV Uploaded successfully")
        if input_csv.name.endswith("csv"):
            data = pd.read_csv(input_csv)
        else:
            data = pd.read_excel(input_csv)
        st.dataframe(data, use_container_width=True)

    with col2:
        st.info("Chat with CSV File")

        input_text = st.text_area("Enter your query")

        if input_text is not None:
            if st.button("Chat with CSV"):
                st.info("Your Query: " + input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)
