# langchain + Tavily
import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch
from tavily import TavilyClient

tavily = TavilyClient()


@tool  # converts the function to a langchain tool
# not using any more.
def search(query: str) -> str:
    """
    Tool that searched over the internet

    Args:
        query: The query to search for.

    Returns:
        The Search Result.
    """

    print(f"Searching for {query}")
    return tavily.search(query=query)


# Source defination for the LLM
class Source(BaseModel):
    """Schema for source used by the agent"""

    url: str = Field(description="the URL of the source")


# agent response formatter
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""

    answer: str = Field(description="THe agent's Response to the query")

    sources: List[Source] = Field(
        default_factory=list,
        description="The list of sources used to generate the ans: ",
    )


# LLM definiation and tools initialization.
llm = ChatAnthropic(
    base_url=os.environ["FCC_BASE_URL"].removesuffix("/v1"),
    api_key=os.environ["FCC_API_KEY"],
    model=os.environ["FCC_MODEL"],
    temperature=0,
)
tools = [
    TavilySearch()
]  # add the tool that you create here in this case i am just using the inbuild Tavily search but you could use ur search function as well in here.

structured_llm = llm.with_structured_output(
    AgentResponse
)  # this is the llm that structres it

# Normal Agent defination
agent = create_agent(
    model=llm, tools=tools
)  # response-format can also be used in case of chatgpt


def section3():
    print("Section 3 for Ai agents")

    # invoking the LLM with the values
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="search for 3 job openings for Frontend and UI developer senior role in germany posted in the last 24 hours on linkedIn and list them out here with the apply link in a table"
                )
            ]
        }
    )
    final_message = result["messages"][-1]

    # Structring it in the required format here.
    response = structured_llm.invoke(f"""
        Convert it to the correct structure
        Agent Response:

        {final_message.content}
        """)

    print(response)


if __name__ == "__main__":
    section3()
