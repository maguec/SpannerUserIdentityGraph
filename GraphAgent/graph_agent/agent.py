from google.adk.agents import Agent
from google.adk.tools.toolbox_tool import ToolboxTool

toolbox = ToolboxTool("http://127.0.0.1:5000")
tools = toolbox.get_toolset(toolset_name='query-email')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='email_agent',
    description='Answer questions about the email addresses in the Spanner database',
    instruction='Extract the email address from the question and query the query-email tool in the Spanner database',
    tools=tools,
)
