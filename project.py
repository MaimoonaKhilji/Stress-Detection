import streamlit as st

# Add the CSS file to the app
with open("custom.css", "r") as f:
    css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Use the CSS styles in the app
st.title("My Beautiful App")
st.write("This is a beautiful app.")
