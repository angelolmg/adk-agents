from google.adk.agents.llm_agent import Agent

# Import modular specialist agents
from .work_routine_agent import work_routine_agent
from .academic_reviewer import academic_reviewer
from .research_agent import root_agent as research_pipeline

# Configure the description for ResearchPipeline so the router can delegate to it
research_pipeline.description = (
    "Especialista em realizar pesquisas estruturadas na web sobre temas acadêmicos, "
    "buscar artigos/referências, classificar fontes e gerar resumos detalhados."
)

# Coordinator/Routing Agent
router_agent = Agent(
    model='gemini-2.5-flash',
    name='router_agent',
    description='Coordenador principal que direciona as solicitações do usuário para os especialistas corretos.',
    instruction=(
        "You are the main coordinator. Your job is to understand the user's intent and route the conversation to the correct specialist sub-agent:\n"
        "- Delegate to `work_routine_agent` for anything related to work routine, calendar events, tasks, or schedules (saving, listing, deleting).\n"
        "- Delegate to `academic_reviewer` for academic text review, grammar checks, or reading PDF/LaTeX files.\n"
        "- Delegate to `ResearchPipeline` for academic web research, literature search, ranking/grading sources, and generating structured summaries on specific research topics.\n\n"
        "Rules:\n"
        "1. Converse in English by default.\n"
        "2. Route immediately as soon as you identify the user's intent. Do not answer questions yourself if they belong to one of the specialists."
    ),
    sub_agents=[work_routine_agent, academic_reviewer, research_pipeline]
)

# Expose router_agent as the root_agent for the app
root_agent = router_agent

from google.adk.apps import App

app = App(root_agent=root_agent, name="app")




