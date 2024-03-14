import streamlit as st
import json

# This is where we will indicate that we will have a multi-page app
st.set_page_config()

# We can use our file structure 
with open('config/filepaths.json', 'r') as f:
    FPATHS = json.load(f)


st.image(FPATHS['images']['banner'])

st.title('Choose page on sidebar:')
st.subheader('Examine the training data or apply the model')

## Next create a pages folder and add the .py files for each page of the app