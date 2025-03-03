import streamlit as st
import pandas as pd
import requests

# Flask API endpoint
api_url = 'https://server-omega-tan-51.vercel.app/data'

# Fetch data from Flask API
response = requests.get(api_url)

# Debugging print statement
if response.status_code == 200:
    st.write("Data fetched successfully!")
    data = response.json()
    st.write(data)  # Check the raw data coming from Flask
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.write("Error fetching data")
