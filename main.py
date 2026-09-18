import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

llm = ChatOpenAI(
    model=os.environ["FCC_MODEL"],
    base_url=os.environ["FCC_BASE_URL"],
    api_key=os.environ["FCC_API_KEY"],
    temperature=0, # low values makes it factual deterministic 0.3 ---- high values 0.8 - 1 are for fiction poetry and creativity
    use_responses_api=True,
    output_version="responses/v1",
)

# llm = ChatNVIDIA(
#     model= 'nvidia/nemotron-3-super-120b-a12b',
#     nvidia_api_key=os.environ["NVIDIA_NIM_API_KEY"],
#     temperature=0,
#     max_retries=3
# )

def main():
    response = ""
    information = """Guild Wars 2 is the fourth major entry in the Guild Wars series and claims to be unique in the MMO genre[4] by featuring a storyline that is responsive to player actions,[5] something which is common in single player role-playing games but rarely seen in multiplayer ones. A dynamic event system replaces traditional questing,[6] utilising the ripple effect to allow players to approach quests in different ways as part of a persistent world. Also of note is the combat system, which aims to be more dynamic than its predecessor by promoting synergy between professions and using the environment as a weapon,[7][8] as well as reducing the complexity of the Magic-style skill system of the original game.

As a sequel to Guild Wars, Guild Wars 2 features the same lack of subscription fees that distinguished its predecessor from other commercially developed online games of the time, though until August 2015 a purchase was still required to install the game.[9] The game sold over two million copies in its first two weeks.[10][11] By August 2013, the peak player concurrency had reached 460,000.[12] By August 2015, over 5 million copies had been sold, at which point the base game became free-to-play.[13] By August 2021, over 16 million accounts have been created.[14] On August 16, 2022, it was announced that Guild Wars 2 will be releasing on Steam as part of the game's 10th anniversary celebration.[15]

Six major expansion packs have been released for the game; Heart of Thorns (2015), Path of Fire (2017), End of Dragons (2022), Secrets of the Obscure (2023), Janthir Wilds (2024), and Visions of Eternity (2025).[16][17] Each expansion pack introduces new content, including new regions of the world to explore, end-game encounters and masteries, with the first three also offering new professions, elite specializations, and seasons of 'Living World'; live content updates that continue expansion storylines and bridge the gap between them.[18] In February 2023, it was announced that future Guild Wars 2 expansions starting with Secrets of the Obscure would be adopting a new release model. Instead of releasing every two to four years with a season of Living World in between, smaller scale expansions would be released more frequently at a slightly reduced price. Additional content for these expansions will then be added through quarterly releases.[19] In June 2026, alongside the announcement of Guild Wars 3, it was announced that the development team would be pausing Guild Wars 2 expansion development, with the intention of resuming annual expansions following the sequel's release.[20]

"""
    summary_template = """
    given the information {information} about a game I want you to create:
    1. A short summary
    2. two interesting facts about the game
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    chain = summary_prompt_template | llm

    # chunk way of doing it
    for chunk in chain.stream({
        "information": information
    }):
        response += chunk.text

    # normal invoke
    # response = chain.invoke({"information": information})

    print(f"Reponse: {response}")




if __name__ == "__main__":
    main()
