from google.adk.agents import Agent

from .tools import search_semantic_scholar
from .tools import search_arxiv

root_agent = Agent(
    name="research_agent",

    model="gemini-2.5-flash-lite",

    instruction="""
    You are a research assistant.

    When the user asks for papers on a topic,
    if is not specified, search BOTH Semantic Scholar and arXiv.

    Summarize the results.

    Avoid duplicates.
    """,

    tools=[
        search_semantic_scholar,
        search_arxiv,
    ],
)