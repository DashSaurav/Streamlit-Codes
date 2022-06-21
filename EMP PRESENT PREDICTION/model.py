import pickle
import streamlit as st
from PIL import Image
import pandas as pd

img = Image.open("MicrosoftTeams-image.png")
col = st.columns(4)
with col[1]:
    st.image(img, width=300)

import datetime 
# date=str(input('Enter the date(for example:09 02 2019):'))
# date_input = st.date_input("Input a Date",datetime.date(2022, 6, 6))
# st.write(date_input)
# day_name= ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# day = datetime.datetime.strptime(str(date_input), '%Y-%M-%d').weekday()
# st.write(day_name[day-2]) 
# year = date_input.strftime("%Y")
# day = date_input.strftime("%d")
# month = date_input.strftime("%m")
# st.write(year)
# st.write(month)
# st.write(day)

st.header("Present Absent Prediction.")
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
        day_name= ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        val = datetime.datetime.strptime(str(date_input), '%Y-%M-%d').weekday()
        Day = day_name[val-2]
        st.write(Day)
        # Day = st.selectbox('Select Day',('wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday','tuesday'))
    with c[2]:
        # day_name= ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        # Day = datetime.datetime.strptime(str(date_input), '%Y-%M-%d').weekday()
        # st.write(day_name[Day-2])
        Year = st.slider('Select Year',2022,2023,2022)
    cc = st.columns(3)
    with cc[0]:
        # Year = date_input.strftime("%Y")
        # st.write(Year)
        Month = st.slider('Select Month',1,12,6)
    with cc[1]:
        # Month = date_input.strftime("%m")
        # st.write(Month)
        Date = st.slider('Select Date',1,31,6)    
    with cc[2]:
        # Date = date_input.strftime("%d")
        # st.write(Date)
        some_new = st.slider('Select some value',1,31,6)    

    data = {'Name':[Name],'Day':[Day], 
            'Year':[Year],'Month':[Month],'Date':[Date],
            }
    features = pd.DataFrame(data)
    return features

input_df = user_input_features()
# st.write(input_df)

churn_raw = pd.read_csv("absent.csv")
churn_raw.fillna(0, inplace=True)
churn = churn_raw.drop(columns=['Present'])
df = pd.concat([input_df,churn],axis=0)

encode = ['Name','Day']
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
       'Name_smitha', 'Name_utkarsh', 'Name_zeba', 'Day_friday', 'Day_monday',
       'Day_saturday', 'Day_sunday', 'Day_thursday', 'Day_tuesday',
       'Day_wednesday', 'Year', 'Month', 'Date']
df = df[features]

# st.subheader('User Input features')
# st.write(df)
st.subheader("Prediction.")
load_clf = pickle.load(open('present_absent.pkl', 'rb'))

prediction = load_clf.predict(df)
if prediction == 0:
    prediction = "Employee will be Absent"
    st.error(prediction)
else:
    prediction = "Employee will be Present"
    st.info(prediction)
