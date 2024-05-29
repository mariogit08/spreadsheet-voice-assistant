from pyt2s.services import stream_elements
from playsound import playsound

def speak_text(text):

    obj = stream_elements.StreamElements()
    data = obj.requestTTS(text)

    audio_file_path = 'audio/ttsaudio.mp3'
    with open(audio_file_path, 'wb') as file:
        file.write(data)

    print(f"Audio saved to '{audio_file_path}'.")
    playsound(audio_file_path)
