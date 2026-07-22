from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

"""Tools that our Simple Chatbot can use"""
@tool 


def greeting(name: str) -> str:
    """Used when greeting the user"""
    return f"Hello {name}, How are you doing?"
def add(a: float, b: float) -> str:
    """Used when preforming addition calculations with numbers"""
    return f"The sum of {a} and {b} = {a + b}"
def multiply(a: float, b: float) -> str:
    """Used when preforming multiplucation calculations with numbers"""
    return f"The sum of {a} and {b} = {a * b}"
def subtract(a: float, b: float) -> str:
    """Used when preforming subtraction calculations with numbers"""
    return f"The sum of {a} and {b} = {a - b}"
def divide(a: float, b: float) -> str:
    """Used when preforming division calculations with numbers"""
    return f"The sum of {a} and {b} = {a / b}"
    
def main():
    model = ChatOpenAI(temperature = 0)
    tools = [add, multiply, subtract, divide, greeting]
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assitant. Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower == "quit":
            break
        
        print("\nAssitant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end='')
        print()
        
if __name__ == "__main__":
    main()