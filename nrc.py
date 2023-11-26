import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64
import time

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio as WAV file
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_bytes = audio_file.getvalue()
    
    # Encode the audio in base64
    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    
    # Generate the audio element with autoplay
    audio_element = f'<audio src="data:audio/wav;base64,{audio_base64}" controls="controls" autobuffer="autobuffer" autoplay="autoplay"></audio>'
    
    return audio_element

def countdown_timer(durations, language='en'):
    st.write(f"Countdowns started for the following durations: {', '.join(map(str, durations))} seconds.")
    
    for duration in durations:
        st.write(f"Countdown started for {duration} seconds.")
        
        # TTS for the start of the countdown
        st.markdown(text_to_speech(f"{duration} seconds countdown starts now", language=language), unsafe_allow_html=True)
        time.sleep(1)

        # Automatic countdown with TTS announcements for each second
        for i in range(duration, 0, -1):
            st.write(f"Time remaining: {i} seconds")
            st.markdown(text_to_speech(str(i), language=language), unsafe_allow_html=True)
            time.sleep(1)
        
        # TTS for the end
        st.success(f"Time's up for {duration} seconds!")
        st.markdown(text_to_speech(f"Time's up for {duration} seconds!", language=language), unsafe_allow_html=True)

def main():
    st.title("Streamlit Countdown Timer with TTS")

    # Sidebar for user input
    with st.sidebar:
        st.header("Settings")
        durations = [st.number_input(f"Enter duration {i+1} (seconds)", min_value=1, value=60, step=1) for i in range(20)]
        language = st.selectbox("Select TTS language", ["en", "ja", "es", "fr", "de"], index=0)

    # Button to start the countdown
    if st.button("Start Countdowns"):
        countdown_timer(durations, language=language)

if __name__ == "__main__":
    main()
