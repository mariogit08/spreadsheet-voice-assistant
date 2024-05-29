from ollama import Client

ollama_client = Client(host='http://localhost:11434')

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
            'content': "You are a spreadsheet data assistant analyser that gives very short answers about .csv data, the answers need to be very short",
        },
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return response
