import streamlit as st

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

#st.title("Voice Over Input")

# Initialize session state
if 'audio_bytes' not in st.session_state:
    st.session_state.audio_bytes = None

# Create a record button with an icon
user_input = st.text_input("Enter your text here:")
# Display the user's input 
if user_input: 
    st.write("You entered:", user_input)

# Use columns to place buttons side by side 
col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button("🎙️ Record1", key='k1'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        st.session_state.message = "C:/Users/NChunduri/Downloads/find_the_duplicates.wav"        
with col2:
    if st.button("🎙️ Record2", key='k2'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        audio_file = "C:/Users/NChunduri/Downloads/find_the_common_data_points.wav"
with col3:
    if st.button("🎙️ Record3", key='k3'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        audio_file = "C:/Users/NChunduri/Downloads/give_me_debt_or_equity_ratio.wav"
with col4:
    if st.button("🎙️ Record4", key='k4'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        audio_file = "C:/Users/NChunduri/Downloads/give_me_earnings_per_share.wav"
with col5:
    if st.button("🎙️ Record5", key='k5'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        audio_file = "C:/Users/NChunduri/Downloads/give_me_the_inflation_rate_in_US.wav"
with col6:
    if st.button("🎙️ Record6", key='k6'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
        audio_file = "C:/Users/NChunduri/Downloads/give_me_the_max_roe_for_year_2022.wav"

st.write("audio file:", audio_file)

# Convert speech to text
with sr.AudioFile(st.session_state.message) as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print("The Voice You Have Given Is:")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")