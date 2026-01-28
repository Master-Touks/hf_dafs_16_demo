import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Best rec_app ever! GO STEELERS",
    page_icon="🦠",
    layout="wide"
)

st.title("REC_APP DAWG!!!!!!!!!!")

st.write("""
    REC_APP du cours de streamlit et pq pas d'autres cours...
""")

data = px.data.carshare()
new_columns = {
    "centroid_lat": "latitude", "centroid_lon": "longitude"
}
data.rename(columns=new_columns, inplace=True)
unique_hours = data.peak_hour.sort_values().unique()

st.write(data.head())

peak_hours_selected = st.selectbox(label="select a peak hour", options=unique_hours, index=None)

if peak_hours_selected: # comportement utilisateur
    st.map(data=data[data["peak_hour"] == peak_hours_selected], latitude=data["latitude"], longitude=data["longitude"])


else: # comportement par défault
    st.map(data=data, latitude=data["latitude"], longitude=data["longitude"])