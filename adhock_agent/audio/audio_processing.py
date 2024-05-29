import speech_recognition as sr
from pydub import AudioSegment
from whisper import load_model
from text.text_to_speech import speak_text

whisper_model = load_model("base")

def listen_to_user():
    recognizer = sr.Recognizer()
    mp3_file_path = "audio/output.mp3"

    with sr.Microphone() as source:
        speak_text("And now, how can I help you?")
        audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=6)
        print("Recording finished.")

    wav_file_path = "audio/temp.wav"
    with open(wav_file_path, "wb") as wav_file:
        wav_file.write(audio_data.get_wav_data())

    audio_segment = AudioSegment.from_wav(wav_file_path)
    audio_segment.export(mp3_file_path, format="mp3")

def transcribe_audio_to_text():
    print("Listening for voice command...")
    result = whisper_model.transcribe("audio/output.mp3", language='en')
    return result['text']
