import streamlit as st
import speech_recognition as sr


# Create a record button with an icon
user_input = st.text_input("Enter your text here:")
# Display the user's input 
if user_input: 
    st.write("You entered:", user_input)

# Initialize session state for each button click
if 'message' not in st.session_state:
    st.session_state.message = ""

# Use columns to place buttons side by side
col1, col2,col3, col4,col5, col6   = st.columns(6)

with col1:
    if st.button("🎙️ Record 1", key='button1'):
        st.session_state.message = "find the duplicates from all the three files"

with col2:
    if st.button("🎙️ Record 2", key='button2'):
        st.session_state.message = "find the common data points from balance_sheet,income_Statement,income_balance_statement "
with col3:
    if st.button("🎙️ Record 3", key='button3'):
        st.session_state.message = "give me the max roe for year 2022 for each category and company "

with col4:
    if st.button("🎙️ Record 4", key='button4'):
        st.session_state.message = "give me the nvda inflation rate in US "

with col5:
    if st.button("🎙️ Record 5", key='button5'):
        st.session_state.message = "give me earnings per share and share holder equity for each category for last 5 years "

with col6:
    if st.button("🎙️ Record 6", key='button6'):
        st.session_state.message = "give me debt or equity ratio and revenue from 2005 onwards for each company and Category"



# Display the message
if st.session_state.message:
    st.write("Voice Input Received Is:")
    st.write(st.session_state.message)
