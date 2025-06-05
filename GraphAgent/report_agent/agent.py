from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")
tools = toolbox.load_toolset('reports')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='report_agent',
    description='Generate reports based on the questions associate with question',
    instruction='Generate a report based on the question and display in a table format',
    tools=tools,
)
