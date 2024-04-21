import streamlit as st

st.write("""
# Largest number App

""")
#Get Input

st.header('User Input Parameters')

if "laregstNum" not in st.session_state:
    st.session_state.laregstNum = 0
def largestNum():
  laregstNum = st.session_state.num1_input
  if ( laregstNum < st.session_state.num2_input):
    laregstNum = st.session_state.num2_input
  if ( laregstNum < st.session_state.num3_input):
    laregstNum = st.session_state.num3_input
    
num1 = st.number_input("Number 1",min_value=0,max_value=200000,step=1,value=0,key="num1_input",on_change=largestNum)
num2 = st.number_input("Number 2",min_value=0,max_value=200000,step=1,value=0,key="num2_input",on_change=largestNum)
num3 = st.number_input("Number 3",min_value=0,max_value=200000,step=1,value=0,key="num3_input",on_change=largestNum)


    
st.subheader('The largest Number is')
st.write(st.session_state.laregstNum)
