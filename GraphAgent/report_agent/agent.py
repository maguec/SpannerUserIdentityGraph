from google.adk.agents import Agent
from google.adk.tools.toolbox_tool import ToolboxTool

toolbox = ToolboxTool("http://127.0.0.1:5000")
tools = toolbox.get_toolset(toolset_name='reports')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='report_agent',
    description='Generate reports based on the questions associate with question',
    instruction='Generate a report based on the question and display in a table format',
    tools=tools,
)
