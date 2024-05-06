# Spreadsheet Analysis and Voice Command Bot

This repository contains a Python application that integrates with Ollama and other third-party libraries to analyze spreadsheet data based on voice commands. The application uses voice recognition to listen to user commands, transcribes the audio to text, and provides analysis responses based on the commands. The application also uses text-to-speech functionality to provide audio responses to the user.

## Features

- **Voice Recognition**: Listens for voice commands from the user and transcribes the audio to text using the Whisper model.
- **Spreadsheet Analysis**: Analyzes a given spreadsheet based on user commands. The analysis is powered by the Ollama model to understand the user's commands and provide relevant analysis.
- **Text-to-Speech**: Uses a text-to-speech engine to convert the analysis response into speech, making the results accessible to the user.
- **Audio Feedback**: Provides audio responses using `pyttsx3` and `playsound` to speak the analysis results back to the user.

## Requirements

- Python 3.7 or higher
- Ollama client and server running locally (update host URL if necessary)
- Required Python libraries (specified in `requirements.txt`)

## Installation

Clone this repository:

   ```shell
   git clone https://github.com/your-username/spreadsheet-voice-bot.git
   cd spreadsheet-voice-bot
   pip install -r requirements.txt
```

## Usage
```
python main.py
```
