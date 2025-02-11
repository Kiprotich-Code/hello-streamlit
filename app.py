import streamlit as st 
import requests 

st.title("Flood Detector App Dashboard")

FLASK_SERVER_URL = "https://server-omega-tan-51.vercel.app/data"

# fetching data from the Flask app
def fetch_data():
    try:
        response = requests.get(FLASK_SERVER_URL)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to fetch the data from the server.")
            return []
        
    except Exception as e:
        st.error(f"An error occured: {e}")
        return []
    
data = fetch_data()

# displaying data 
if data:
    st.subheader("The Sensor Data")
    st.table(data)
    
# some visualization
if data:
    st.subheader("Visualization")
    
    water_levels = [entry["water_level"] for entry in data]
    temperatures = [entry["temperature"] for entry in data]
    timestamps = [entry["id"] for entry in data]
    
    st.write("Water level over time")
    st.line_chart(water_levels)
    
    # plotting temperatures
    st.write("Tmeperature over Time")
    st.line_chart(temperatures)

else:
    st.write(f"Error fetching data from: {FLASK_SERVER_URL}")

