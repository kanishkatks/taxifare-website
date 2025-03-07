import streamlit as st
from geopy.geocoders import Nominatim

st.markdown(f"<h1 align = 'center' style='font-size: 48px;'>TaxiFarePred</h1>",unsafe_allow_html=True)

st.image('./Taxi_image01.jpg')

st.markdown('''
This app will provide taxifares in the city of NY based data until 2015 ''')

col1, col2 = st.columns(2)





with col1:
    st.write('Pick up location')
    pick_add = st.text_input(label = 'Enter the pickup address')
    date_ =st.date_input('Enter a date')
    # p_lon = st.number_input(label='Enter the pickup longitude', min_value=-74.7,max_value=-74.3)
    # p_lat = st.number_input(label= 'Enter the pickup latitude', min_value =40.5, max_value=40.9)

with col2:
    st.write('Drop up location')
    drop_add = st.text_input(label = 'Enter the DropOff address')
    time_ =st.time_input(label='Time of pickup',)
    # d_lon =st.number_input(label='Enter the dropoff longtitude', min_value=-74.7,max_value=-74.3)
    # d_lat = st.number_input(label= 'Enter the dropoff latitude', min_value =40.5, max_value=40.9)

pass_count = st.select_slider('Number of people:', ['1','2', '3', '4','5'])

geolocator = Nominatim(user_agent="geoapi_explorer")  # Set a unique user agent
pick_loc = geolocator.geocode(pick_add)
drop_loc = geolocator.geocode(drop_add)



url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


#2.
params = {
    'pickup_datetime': f'{date_} {time_}',
    'pickup_longitude': pick_loc.longitude ,
    'pickup_latitude':  pick_loc.latitude,
    'dropoff_longitude': drop_loc.longitude,
    'dropoff_latitude': drop_loc.latitude,
    'passenger_count': pass_count,
}
import requests
respone = requests.get(url, params=params).json()



st.markdown(f"<h1 style='font-size: 48px;'>Predicted Taxi Fare: ${respone['fare']:.2f}</h1>",unsafe_allow_html=True)
