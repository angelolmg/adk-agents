from google.adk.agents import LlmAgent

summary_agent = LlmAgent(
    name="SummaryAgent",

    model="gemini-2.5-flash",

    instruction="""
    Using these ranked papers:

    {ranked_papers}

    Generate

    - overview
    - research themes
    - top 5 papers
    - recommended reading order
    - future research directions

    Be concise.
    """,

    output_key="final_report",
)