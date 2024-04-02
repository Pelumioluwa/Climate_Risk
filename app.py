import streamlit as st

def greet(name):
    return f"Hello, {name}!"

# Create a text input field for the user's name
name = st.text_input("Enter your name")

# If the input field is not empty, call the greet function and display the result
if name:
    greeting = greet(name)
    st.write(greeting)