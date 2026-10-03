## Section 3: The GIST of Ai Agents

Introduction:
Agents: An agent is a software system that uses LLMs as a reasoning engine to decide what actions to take, and then execute those actions.

Agents V/S chains

UNlike simple chains in runables, where the sequenc of the actions are hard coded agents dynamically which tools or steps need to be taken to solve a specific task or to answer specific questions.

The LLMs in the agent decides what to do next. But in chains we use LLMs o maybe summarize something or generate some text. But we has devs define the control flow.

Chain: Developer defined control flow
Agents: LLM defined control flow

Agent = LLM + tools (Api search, execute code, collect data etc.)

reAct Agent High level
And it's a specific type of an agent architecture that follows the react paradigm. Now the name react comes from reasoning in acting. 


            -------------Finishes----------------->
            |                                      |
query ---> thinks ---> Actions ---> tools       Answer 
            |                           |
            <-------observation----------


Tools:

A tool is basically a fucntion that an AI agent can execute.

