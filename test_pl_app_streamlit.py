import streamlit as st
import requests
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def get_players_data():
    # Get general information
    response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = response.json()

    # Convert players data to DataFrame
    players_df = pd.DataFrame(data['elements'])

    return players_df

if st.button('Get Players Data'):
    players_df = get_players_data()
    st.write(players_df)

options = st.sidebar.multiselect(
    'Choose models to predict your team',
    ['Decision Tree', 'XG Boost Regressor', 'CatBoost', 'LightGBM', "Hugging Face"],
    placeholder= "Choose an Option"
)
