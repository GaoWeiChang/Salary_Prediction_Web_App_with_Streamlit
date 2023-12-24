import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

'''
To run and open website : streamlit run app.py
'''

# for execute 
page = st.sidebar.selectbox("Explore or Predict the salary", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()