'''

This is a script to run all the tools in the langchain library. It is meant to be used as a reference for how to use the library.
https://github.com/hwchase17/langchain/blob/master/docs/modules/agents/tools/getting_started.md

'''


from langchain. agents import load_tools
from langchain. agents import initialize_agent
from langchain. agents import AgentType
from langchain. memory import ConversationBufferMemory
from langchain. chat_models import ChatOpenAI
import os
import credentials
from newsapi import NewsApiClient



#%%
# set up openai api key
openai_api_key = os.environ.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = credentials. OPENAI_API_KEY
os.environ["GOOGLE_API_KEY"] = credentials. google_api_key
os.environ["GOOGLE_CSE_ID"] = credentials. google_cse_id
os.environ["WOLFRAM_ALPHA_APPID"] = credentials. wolfram_alpha_appid
#os.environ["NEWS_API_KEY"] = credentials.news_api_key

#newsapi = NewsApiClient(api_key='...')

memory = ConversationBufferMemory()
llm = ChatOpenAI( )
tools = load_tools([
   'wikipedia',
   'llm-math',
   'google-search',
   'python_repl',
   'wolfram-alpha',
   'terminal',
   #'news-api',
   #'podcast-api',
   #'openweathermap-api'
 ], llm=llm)
agent = initialize_agent(
     tools,
     llm,
     agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
 )


def get_prompt_input_key(inputs, memory_variables):
    input_keys = list(inputs.keys())

    for key in memory_variables:
        if key in input_keys:
            return key

    raise ValueError(f"One input key expected got {input_keys}")

agent.run({'chat_history': [], 'input': "What's up ChatGPT?"})

