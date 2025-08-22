import pyttsx3
import streamlit as st
import os
import time

# text = "Hello, this is a test of the text-to-speech system."    
# engine.say(text)
# engine.runAndWait() 
tts_dir = os.path.join(os.getcwd(), "tts_voice")

if not os.path.exists(tts_dir):
    os.makedirs(tts_dir)
st.write("Voice Transfer Application")
st.write("This application allows you to transfer voice using a text-to-speech model.")
engine1 = pyttsx3.init()
voices = engine1.getProperty('voices')
voiceid = st.radio("Select Voice", options=[voice.id for voice in voices], index=0)

volume = st.slider('Speech Volume select', 0, 100, 25)
rate = st.slider('speech rate select', 0, 200, 100)
text = st.text_input("Enter text to convert to speech", key="text_input")
if text:
    try:
       with st.spinner("Converting text to speech...",show_time=True):
            voice_path = os.path.join(tts_dir, str(int(time.time())))
            print(voice_path)
            engine = pyttsx3.init()
            engine.setProperty('rate', rate)  # Set speech rate
            engine.setProperty('volume', volume/100)  # Set volume level (0.0 to 1.0)
            
            engine.setProperty('voice', voiceid)  # Set to a Chinese voice on macOS
           
            ##tts = gTTS(text=text, lang='zh')
            print(voice_path)
            print(f"完整路径：{os.path.abspath(voice_path+'.mp3')}")  # 验证路径
            print(f"目录可写：{os.access(os.path.dirname(voice_path), os.W_OK)}")  # 检查权限
            engine.save_to_file(text, voice_path + '.mp3')
            engine.say(text)
            engine.runAndWait() 
            st.audio(f'{voice_path}.mp3', format='mp3/audio/wav',loop=False)  
            st.write("Audio file saved successfully.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter text to convert to speech.")
