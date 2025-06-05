from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")
tools = toolbox.load_toolset('shapes')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='shape_agent',
    description='Given an zip code, last 4, email address and a shipping address look for similar transaction shap',
    instruction='Extract the email address, last4 credit card digits, zipcode, and shipping address search from the question and query the toolbox to return the timestamp, is_suspect and the similar shipping address as a table',
    tools=tools,
)
