import streamlit as st

st.title("Voice Over Input")

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
with col2:
    if st.button("🎙️ Record2", key='k2'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
with col3:
    if st.button("🎙️ Record3", key='k3'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
with col4:
    if st.button("🎙️ Record4", key='k4'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
with col5:
    if st.button("🎙️ Record5", key='k5'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic
with col6:
    if st.button("🎙️ Record6", key='k6'):
        st.session_state.audio_bytes = b"Dummy audio data"  # Replace this with actual audio recording logic

# Display the recorded audio if available
#if st.session_state.audio_bytes:
#   st.audio(st.session_state.audio_bytes)
