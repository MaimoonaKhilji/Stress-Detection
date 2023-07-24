# app.py

import streamlit as st

def main():
    # Load your custom CSS file
    st.markdown('<link href="custom.css" rel="stylesheet">', unsafe_allow_html=True)

    st.title('Custom Theme Example')
    st.write('This is a Streamlit app with a custom theme!')

if __name__ == '__main__':
    main()
