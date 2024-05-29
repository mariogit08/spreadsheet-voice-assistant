import pandas as pd
from audio.audio_processing import listen_to_user, transcribe_audio_to_text
from llm.spreadsheet_analysis import analyze_spreadsheet
from text.text_to_speech import speak_text

def main():
    df = pd.read_csv('../data/sales_data.csv', sep=",", encoding='Latin-1')

    while True:
        listen_to_user()
        command = transcribe_audio_to_text()
        print(f"Voice command received: {command}")

        speak_text("Thinking..")
        response = analyze_spreadsheet(command, df)
        print(f"Analysis response: {response['message']['content']}")

        speak_text(response['message']['content'])

if __name__ == '__main__':
    main()
