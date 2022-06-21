import pickle
import streamlit as st
from PIL import Image
import pandas as pd
import datetime 
import time
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_download = "https://assets3.lottiefiles.com/packages/lf20_jxdtgpuk.json"
lottie_download = load_lottieurl(lottie_url_download)

img = Image.open("MicrosoftTeams-image.png")
col = st.columns(4)
with col[1]:
    st.image(img, width=300)

st.header("Employee Absenteeism Prediction")
def user_input_features():
    c = st.columns(3)
    with c[0]:
        Name = st.selectbox('Name of Employee',('Priya ', 'Gourav', 'Rishi', 'saurav', 'neha', 'arun', 'abhishek',
       'mayank', 'neeraj', 'prince', 'singh', 'arjun', 'ajay', 'ayush',
       'priyanka', 'shantanu', 'mehak', 'poorvi', 'sidhika', 'hunny',
       'ishan', 'sachin', 'rohan', 'rohit', 'jatin', 'utkarsh', 'Aman',
       'Ritik', 'Rohit', 'Prena', 'Tripti', 'Rajvir', 'Ranvir', 'Neha',
       'Pawan', 'Kajal', 'siddhart', 'Anjali', 'Ayushi', 'smitha', 'zeba',
       'Niharika', 'Arjun', 'Ajith', 'Tejaswani', 'Nilisha', 'Akansha',
       'Abrajith', 'Arun', 'Raunak', 'sanjay'))
    with c[1]:
        date_input = st.date_input("Select a Date",datetime.date(2022, 6, 6))
        Day = date_input.strftime("%A")
        # st.write(Day)
    with c[2]:
        Reasons = st.selectbox("Select a Reason",('None','Health Issues', 'Public Holiday', 'Weekend', 'Weather','DOB'))
   
    data = {'Name':[Name],'Day':[Day], 
            'Reasons':[Reasons],
            }
    features = pd.DataFrame(data)
    return features

input_df = user_input_features()
# st.write(input_df)

churn_raw = pd.read_csv("absent_data.csv")
churn_raw.fillna(0, inplace=True)
churn = churn_raw.drop(columns=['Present'])
df = pd.concat([input_df,churn],axis=0)

encode = ['Name','Day','Reasons']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df,dummy], axis=1)
    del df[col]
df = df[:1] # Selects only the first row (the user input data)
df.fillna(0, inplace=True)

features = ['Name_Abrajith', 'Name_Ajith', 'Name_Akansha', 'Name_Aman',
       'Name_Anjali', 'Name_Arjun', 'Name_Arun', 'Name_Ayushi', 'Name_Gourav',
       'Name_Kajal', 'Name_Neha', 'Name_Niharika', 'Name_Nilisha',
       'Name_Pawan', 'Name_Prena', 'Name_Priya ', 'Name_Rajvir', 'Name_Ranvir',
       'Name_Raunak', 'Name_Rishi', 'Name_Ritik', 'Name_Rohit',
       'Name_Tejaswani', 'Name_Tripti', 'Name_abhishek', 'Name_ajay',
       'Name_arjun', 'Name_arun', 'Name_ayush', 'Name_hunny', 'Name_ishan',
       'Name_jatin', 'Name_mayank', 'Name_mehak', 'Name_neeraj', 'Name_neha',
       'Name_poorvi', 'Name_prince', 'Name_priyanka', 'Name_rohan',
       'Name_rohit', 'Name_sachin', 'Name_sanjay', 'Name_saurav',
       'Name_shantanu', 'Name_siddhart', 'Name_sidhika', 'Name_singh',
       'Name_smitha', 'Name_utkarsh', 'Name_zeba', 'Day_Friday', 'Day_Monday',
       'Day_Saturday', 'Day_Sunday', 'Day_Thursday', 'Day_Tuesday',
       'Day_Wednesday', 'Reasons_DOB', 'Reasons_Health Issues', 'Reasons_None',
       'Reasons_Public Holiday', 'Reasons_Weather', 'Reasons_Weekend']
df = df[features]

# st.subheader('User Input features')
# st.write(df)

st.subheader("Prediction.")
load_clf = pickle.load(open('present_absent_new_model.pkl', 'rb'))

prediction = load_clf.predict(df)
col = st.columns(3)
with col[1]:
    if prediction == 0:
        with st_lottie_spinner(lottie_download, key="download", height=200,width=200):
            time.sleep(2)
            prediction = "Employee will be Absent"
            st.error(prediction)
    else:
        with st_lottie_spinner(lottie_download, key="download", height=200,width=200):
            time.sleep(2)
            prediction = "Employee will be Present"
            st.info(prediction)
