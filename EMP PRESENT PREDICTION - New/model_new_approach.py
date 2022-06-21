import pickle
import streamlit as st
from PIL import Image
import pandas as pd
import datetime 

#image at header
img = Image.open("MicrosoftTeams-image.png")
col = st.columns(4)
with col[1]:
    st.image(img, width=300)

st.header("Employee Absenteeism Prediction")
# function for taking input
def user_input_features():
    c = st.columns(3)
    with c[0]:
        global Name
        Name = st.selectbox('Name of Employee',('Priya ', 'Gourav', 'Rishi', 'saurav', 'neha', 'arun', 'abhishek',
       'mayank', 'neeraj', 'prince', 'singh', 'arjun', 'ajay', 'ayush',
       'priyanka', 'shantanu', 'mehak', 'poorvi', 'sidhika', 'hunny',
       'ishan', 'sachin', 'rohan', 'rohit', 'jatin', 'utkarsh', 'Aman',
       'Ritik', 'Rohit', 'Prena', 'Tripti', 'Rajvir', 'Ranvir', 'Neha',
       'Pawan', 'Kajal', 'siddhart', 'Anjali', 'Ayushi', 'smitha', 'zeba',
       'Niharika', 'Arjun', 'Ajith', 'Tejaswani', 'Nilisha', 'Akansha',
       'Abrajith', 'Arun', 'Raunak', 'sanjay'))
    with c[2]:
        global Day
        date_input = st.date_input("Select a Date",datetime.date(2022, 6, 6))
        Day = date_input.strftime("%A")
        # st.write(Day)
   
    data = {'Name':[Name],'Day':[Day],}
    
    features = pd.DataFrame(data)
    return features

input_df = user_input_features()
# st.write(input_df)

# call data and do encoding and fitting here.
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
       'Day_Wednesday']
df = df[features]

# st.subheader('User Input features')
# st.write(df)

st.subheader("Prediction.")
load_clf = pickle.load(open('present_absent_new_model.pkl', 'rb'))
load_new = pickle.load(open('some_new_model.pkl', 'rb'))

prediction = load_clf.predict(df)
col = st.columns(3)
with col[1]:
    if prediction == 0:
        prediction = "Employee will be Absent"
        pred_val = 0
        st.error(prediction)
    else:
        prediction = "Employee will be Present"
        pred_val = 1
        st.info(prediction)

# predict_new = load_new.predict(df_new)
# st.write(Name)
# st.write(Day)
# st.write(pred_val)

data_new = {'Name':[Name],'Day':[Day], 
        'Present':[int(pred_val)],
        }
features_new = pd.DataFrame(data_new)
# st.write(features_new)

df_10 = churn_raw[['Name','Day','Present','Reasons']]
churn_new = df_10.drop(columns=['Reasons'])
df_new = pd.concat([features_new,churn_new],axis=0)

# st.write(df_new.tail(5))

encode = ['Name','Day']
for col in encode:
    dummy = pd.get_dummies(df_new[col], prefix=col)
    df_new = pd.concat([df_new,dummy], axis=1)
    del df_new[col]
df_new = df_new[:1] # Selects only the first row (the user input data)
df_new.fillna(0, inplace=True)

features_new = ['Present', 'Name_Abrajith', 'Name_Ajith', 'Name_Akansha', 'Name_Aman',
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
       'Day_Wednesday']
df_new = df_new[features_new]

predict_new = load_new.predict(df_new)
if pred_val == 0:
    col = st.columns(3)
    with col[1]:
        if predict_new[-1] == 'None':
            st.write("No Possible Reason Predicted")
        else:
            st.write("Possible Reason: ",predict_new[-1])