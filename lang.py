import pandas as pd
from ollama import Client
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_community.chat_models import ChatOllama
# LangChain supports many other chat models. Here, we're using Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

optional_params = {
    "top_p": 0.92,
    "repetition_penalty": 1.1,
}

# supports many more optional parameters. Hover on your `ChatOllama(...)`
# class to view the latest available supported parameters
llm = ChatOllama(model="mistral")

prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

# using LangChain Expressive Language chain syntax
# learn more about the LCEL on
# /docs/expression_language/why
chain = prompt | llm | StrOutputParser()

df = pd.read_csv('sales_data_sample.csv',sep=",", encoding='Latin-1')
agent = create_pandas_dataframe_agent(llm, df, verbose=True)

response = agent.run(
    "User: What is the most selled product?"
)

print(response)