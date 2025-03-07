import streamlit as st

st.markdown(f"<h1 align = 'center' style='font-size: 48px;'>TaxiFarePred</h1>",unsafe_allow_html=True)

st.image('./Taxi_image01.jpg')

st.markdown('''
This app will provide taxifares in the city of NY based data until 2015 ''')

col1, col2 = st.columns(2)


date_ =st.date_input('Enter a date')
time_ =st.time_input(label='Time of pickup',)

with col1:
    st.write('Pick up location')
    p_lon = st.number_input(label='Enter the pickup longitude', min_value=-74.7,max_value=-74.3)
    p_lat = st.number_input(label= 'Enter the pickup latitude', min_value =40.5, max_value=40.9)

with col2:
    st.write('Drop up location')
    d_lon =st.number_input(label='Enter the dropoff longtitude', min_value=-74.7,max_value=-74.3)
    d_lat = st.number_input(label= 'Enter the dropoff latitude', min_value =40.5, max_value=40.9)

pass_count = st.select_slider('Number of people:', ['1','2', '3', '4','5'])




url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


#2.
params = {
    'pickup_datetime': f'{date_} {time_}',
    'pickup_longitude': p_lon,
    'pickup_latitude': p_lat,
    'dropoff_longitude': d_lon,
    'dropoff_latitude': d_lat,
    'passenger_count': pass_count,
}
import requests
respone = requests.get(url, params=params).json()



st.markdown(f"<h1 style='font-size: 48px;'>Predicted Taxi Fare: ${respone['fare']:.2f}</h1>",unsafe_allow_html=True)
