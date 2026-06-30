from google.adk.agents import LlmAgent

from .tools import search_all

search_agent = LlmAgent(
    name="SearchAgent",

    model="gemini-2.5-flash",

    instruction="""
    Search scientific literature.

    Always use search_all.

    Return ONLY the list of papers.
    """,

    tools=[search_all],

    output_key="papers",
)