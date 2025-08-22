import streamlit as st
import os
import time
from gtts import gTTS
# gtts need internet
tts_dir = os.path.join(os.getcwd(), "tts_voice")

if not os.path.exists(tts_dir):
    os.makedirs(tts_dir)
st.write("Voice Transfer Application")
st.write("This application allows you to transfer voice using a text-to-speech model.")
text = st.text_input("Enter text to convert to speech", key="text_input")
if text:
    try:
       with st.spinner("Converting text to speech...",show_time=True):
            voice_path = os.path.join(tts_dir, str(int(time.time())))
            print(voice_path)
            tts = gTTS(text=text, lang='zh')
            print(voice_path)
            print(f"完整路径：{os.path.abspath(voice_path+'.mp3')}")  # 验证路径
            print(f"目录可写：{os.access(os.path.dirname(voice_path), os.W_OK)}")  # 检查权限

            with st.spinner("Saving audio file...{voice_path}.mp3'",show_time=True):
                tts.save(voice_path + '.mp3')
                st.audio('{voice_path}.mp3', format='mp3/audio/wav',loop=False)  
                st.write("Audio file saved successfully.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("Please enter text to convert to speech.")



