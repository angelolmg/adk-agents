from google.adk.agents import Agent

from .tools import add_task, list_tasks, remove_task

root_agent = Agent(
    name="todo",

    model="gemini-2.5-flash-lite",

    instruction="""
    Help the user manage tasks.

    Use add_task whenever they ask to create one.

    Use list_tasks whenever they ask what remains.
    """,

    tools=[
        add_task,
        remove_task,
        list_tasks,
    ]
)