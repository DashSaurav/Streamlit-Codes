from csv import writer
import streamlit as st  

st.header("Append Data in CSV File")
name = st.text_input("Enter your Name") 
age = st.number_input("Enter your Age", value=23)
rating = st.slider("Rating of Session", min_value=0, max_value=5, value=0)
remark = st.text_area("Remarks",value="Remark is None")
if st.button("Submit Information"):
    list_data=[name,age,rating,remark]
  
    with open('data.csv', 'a', newline='') as f_object:  
        writer_object = writer(f_object)
        writer_object.writerow(list_data)  
        f_object.close()

    st.info("Data appended successfully.")
