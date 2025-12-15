import streamlit as st
import requests
from dotenv import load_dotenv

load_dotenv()
url = "http://127.0.0.1:8000/rag/query"

def main_layout():
    st.markdown("# RAGtuber")
    st.markdown("An expert YouTuber who knows a lot of Data Engineering!")
    text_input = st.text_input(label="Ask me a question or send a message", key="user_input")
    
    if st.button("Send") and text_input.strip() != "":
        response = requests.post(url, json={"prompt": text_input})
        json_data = response.json()
        st.markdown("## Question/Message:")
        st.markdown(text_input)
        st.markdown("## Answer:")
        st.markdown(json_data.get("answer", "No 'answer' field in response"))

if __name__ == '__main__':
    main_layout()