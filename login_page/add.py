import streamlit as st

st.subheader("Calculator Body.")
col = st.columns(3)
with col[0]:
    n1 = st.number_input("Insert a Number", value = 0, help= "Insert a Higher Number.")
with col[2]:
    n2 = st.number_input("Insert another Number", value = 0, help= "Insert a Smaller number than Previous")

sum = n1+n2
diff = n1-n2
mul = n1*n2

if n1<n2:
    div = n2/n1
elif n1==n2:
    div = 1.0
else:
    div = n1/n2

col1 = st.columns(4)
with col1[0]:
    if st.button("SUM"):
        st.metric(label = "Sum",value = sum)
with col1[1]:
    if st.button("Difference"):
        if diff < 0:
            st.metric(label="Difference",value=-(diff),delta=diff)
        else:
            st.metric(label = "Difference",value = diff,delta=diff)
with col1[2]:
    if st.button("Multiplication"):
        st.metric(label = "Multiplication",value = mul)
with col1[3]:
    if st.button("Division"):
        st.metric(label= "Division", value= div)

