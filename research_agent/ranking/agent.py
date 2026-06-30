from google.adk.agents import LlmAgent

ranking_agent = LlmAgent(
    name="RankingAgent",

    model="gemini-2.5-flash",

    instruction="""
    The following papers were retrieved.

    {papers}

    Tasks

    - remove duplicates
    - rank by relevance
    - preserve every field
    - do not summarize

    Return ONLY the ranked list.
    """,

    output_key="ranked_papers",
)