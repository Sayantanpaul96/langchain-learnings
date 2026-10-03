from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage

from dotenv import load_dotenv

import os

load_dotenv()

llm = ChatAnthropic(
    model_name=os.environ["FCC_MODEL"],
    base_url=os.environ["FCC_BASE_URL"].removesuffix("/v1"),
    api_key=os.environ["FCC_API_KEY"],
    temperature=0
)

agent = create_agent(model=llm)

def section4():
    '''Section 4 of the langchain course'''

    result = agent.invoke(
    {
        "messages": [
            HumanMessage(
                content="Hello to the llm"
            )
        ]
    })
    printable_message = result['messages'][1].content
    print(printable_message)


if __name__ == "__main__":
    section4()