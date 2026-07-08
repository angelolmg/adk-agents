from google.adk.agents import Agent

from .tools import get_weather

root_agent = Agent(
    name="weather_agent",
    model="gemini-2.5-flash-lite",
    instruction="""
    You are a helpful assistant.

    If the user asks about the weather,
    use the get_weather tool.
    """,
    tools=[get_weather],
)