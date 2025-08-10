import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator 🍽️")

cuisine = st.sidebar.selectbox("pick a cuisine ",("Indian","Italian","Mexican","American","African","Japanese"))

if cuisine :
    response = langchain_helper.generate_restaurant_name_and_item(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(',')
    st.write('**menu items**')
    for item in menu_items:
        st.write("-",item)