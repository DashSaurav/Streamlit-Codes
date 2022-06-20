from csv import writer
import streamlit as st  


take_input = st.text_input("Write your Name") 
take_new_input = st.number_input("Enter your Age", value=23)
if st.button("Submit Information"):
    list_data=[take_input,take_new_input]
  
    with open('data.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()

    st.info("Data appended successfully.")