import ollama
from ollama import Client
import pandas as pd
from whisper import load_model
import pyttsx3

# Then use the load_model function
whisper_model = load_model("base")

# Text-to-speech initialization
engine = pyttsx3.init()
engine.setProperty('rate', 90)  # Set speech rate
engine.setProperty('voice', 'com.apple.eloquence.en-US.Shelley')

# Function to listen to voice commands and convert to text
def transcribe_audio_to_text():
    print("Listening for voice command...")
    result = whisper_model.transcribe("output.mp3", language='en')    
    return result['text']

# Ollama model setup
from langchain_community.llms import Ollama

ollama_client = Client(host='http://localhost:11434')
# Function to analyze the spreadsheet according to the command
def analyze_spreadsheet(command, df):
    summary = df.describe().to_string()
    prompt = f"Please analyze the following data summary:\n{summary}\n {command}"
    response = ollama_client.chat(model='llama3:latest', messages=[
        {
            'role': 'user',
            'content': "Can you please express the numbers in my data analysis report as words instead of digit format?",
        },
        {
            'role': 'user',
            'content': "You are a spreedsheet data assistant analyser that gives very short answers about .csv data, the answers need to be very short",
        },        
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response


# Main function
def main():
    # Load the spreadsheet data
    df = pd.read_csv('sales_data_sample.csv',sep=",", encoding='Latin-1')  # Update the file path as needed

    while True:
        listen_to_user()
        command = transcribe_audio_to_text()
        print(f"Voice command received: {command}")

        # Analyze spreadsheet based on the command
        speak_text("I will do my best, don't give up waiting for me!")
        response = analyze_spreadsheet(command, df)
        print(f"Analysis response: {response['message']['content']}")

        # Convert response to speech
        speak_text(response['message']['content'])

from pyt2s.services import stream_elements
from playsound import playsound

def speak_text(text):
    # Initialize StreamElements
    obj = stream_elements.StreamElements()

    # Request TTS audio data
    data = obj.requestTTS(text)

    # Save the audio data to an MP3 file
    audio_file_path = 'ttsaudio.mp3'
    with open(audio_file_path, 'wb') as file:
        file.write(data)

    # Print a message indicating the audio has been saved
    print(f"Audio saved to '{audio_file_path}'.")

    # Play the audio file using playsound
    print("Playing the audio file...")
    playsound(audio_file_path)

import speech_recognition as sr
from pydub import AudioSegment

def listen_to_user():
    recognizer = sr.Recognizer()
    mp3_file_path = "output.mp3"

    with sr.Microphone() as source:
        speak_text("And now, how can I help you?")  

        # Record audio from the microphone
        audio_data = recognizer.listen(source,timeout=15, phrase_time_limit=15)
        print("Recording finished.")

    # Save the audio data as a WAV file
    wav_file_path = "temp.wav"
    with open(wav_file_path, "wb") as wav_file:
        wav_file.write(audio_data.get_wav_data())

    audio_segment = AudioSegment.from_wav(wav_file_path)
    audio_segment.export(mp3_file_path, format="mp3")

if __name__ == '__main__':
    main()
    engine.stop()
