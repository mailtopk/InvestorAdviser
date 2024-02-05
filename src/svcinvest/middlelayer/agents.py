import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import AgentExecutor

import tools
load_dotenv()

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", """
            You are a stock broker, help user's to get latest stock prices and recommendation to buy as of current date.
            You can also calculate the number of to buy or sell if user want to invest x amount of dollars.
        """),
        ("user", "{user_input}"),
        MessagesPlaceholder(variable_name = "agent_notepad")
    ])

def get_agent():
    stock_tools = tools.get_stock_tools()    
    llm = ChatOpenAI( api_key=os.environ['MY_API_Key'],
                   temperature=0, max_retries=2).bind(functions = [format_tool_to_openai_function(f) for f in stock_tools])

    agent =({
            "user_input" : lambda x: x["input"],
            "agent_notepad": lambda x: format_to_openai_function_messages( x["intermediate_steps"]),
            }
            | get_prompt()
            | llm
            | OpenAIFunctionsAgentOutputParser()
        )
    
    open_ai_agent = AgentExecutor.from_agent_and_tools(agent=agent, 
                                tools=stock_tools, 
                                return_intermediate_steps=True, 
                                verbose=False, 
                                handle_parsing_errors=True)
    
    return open_ai_agent

def testagent():
    agent = get_agent()
    result = agent.invoke({"input":"what is the latest stock price of Apple, is it good to buy ?"})
    print(result)

if __name__ == "__main__":
    testagent()

