import streamlit as st

st.set_page_config(page_title="My App", layout="centered")

st.title("🚀 My First Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success(f"Hello {name}! 🎉")
    else:
        st.warning("Please enter your name")
