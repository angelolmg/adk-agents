from google.adk.agents import SequentialAgent

from .search.agent import search_agent
from .ranking.agent import ranking_agent
from .summarizer.agent import summary_agent

root_agent = SequentialAgent(
    name="ResearchPipeline",
    sub_agents=[
        search_agent,
        ranking_agent,
        summary_agent,
    ],
)