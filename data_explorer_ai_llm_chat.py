# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os
import io
import contextlib

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

from groq import Groq

path_cda = '\\CuriosityDataAnalytics'
path_wd = path_cda + '\\wd'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("Data Explorer AI")

with st.sidebar:
    st.image(path_cda + '\\logo.png')

#
#

client = Groq(
    api_key="my_api_key",
)

cols = st.columns(2)

cols[0].subheader('Upload')
file = cols[0].file_uploader('', type=['xlsx'])

if file is not None:
    cols[1].subheader(file.name)
    df = pd.read_excel(file)
    cols[1].dataframe(df, height=220)

    buffer = io.StringIO()
    df.info(buf=buffer)
    df_info = buffer.getvalue()

    with st.container():
        st.subheader('Ask')

        if user_prompt := st.chat_input("Ask", key='ask'):

            full_prompt = f"""
            You are a data scientist analyzing a dataset.
            
            The dataset, named `df`, has already been created and has the following structure:
            {df_info}.
            
            Assume `df` is already available and your task must focus on the entire dataset.
            Assume 'import streamlit as st'.
            
            Your code must only include a string containing a st.write() statement that outputs a very concise sentence describing the result
            that completes the following task related to the 'df' dataset: {user_prompt}.

            Do not provide any code block markers, markdown, explanations, or comments.

            If the question is not related to the 'df' dataset, respond with just an `st.write()` statement advising the user of that.
            """

            message = {'role' : 'user', 'content' : full_prompt}

            if st.button('Clear'):
                st.empty()
            else:
                with st.chat_message("user"):
                    st.markdown(user_prompt)

                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                            messages=[message],
                            model="llama3-8b-8192"
                    )
                    response = stream.choices[0].message.content
                    exec(response)


    
    st.subheader('Aggregate')

    with st.container():
        if user_prompt := st.chat_input("Aggregate", key='aggregate'):

            full_prompt = f"""
            You are a data scientist analyzing a dataset.
            
            The dataset, named `df`, has already been created and has the following structure:
            {df_info}.
            
            Assume `df` is already available and your task must focus on the entire dataset, not just these 5 rows.
            Assume 'import streamlit as st'.
            
            Your code must only include a string containing a st.dataframe() statement that outputs the result
            that completes the following task related to the 'df' dataset: {user_prompt}.

            Do not provide any code block markers, markdown, explanations, or comments.

            If the question is not related to the 'df' dataset, respond with just an `st.write()` statement advising the user of that.
            """

            message = {'role' : 'user', 'content' : full_prompt}

            
            if st.button('Clear'):
                st.empty()
            else:
                with st.chat_message("user"):
                    st.markdown(user_prompt)

                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                            messages=[message],
                            model="llama3-8b-8192"
                    )
                    response = stream.choices[0].message.content
                    exec(response)
                

    st.subheader('Create')

    with st.container():
        if user_prompt := st.chat_input("Create", key='create'):

            full_prompt = f"""
            You are a data scientist analyzing a dataset.
            
            The dataset, named `df`, has already been created and has the following structure:
            {df_info}.
            
            Assume `df` is already available and your task must focus on the entire dataset, not just these 5 rows.
            Assume 'import streamlit as st'.
            Assume 'import plotly.express as px'.
            
            Your code must only include a string containing a 'st.plotly_chart()' statement that outputs the result
            that completes the following task related to the 'df' dataset: {user_prompt}.

            Do not provide any code block markers, markdown, explanations, or comments.

            If the question is not related to the 'df' dataset, respond with just an `st.write()` statement advising the user of that.
            """

            message = {'role' : 'user', 'content' : full_prompt}

            if st.button('Clear'):
                st.empty()
            else:
                with st.chat_message("user"):
                    st.markdown(user_prompt)

                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                            messages=[message],
                            model="llama3-8b-8192"
                    )
                    response = stream.choices[0].message.content
                    exec(response)
