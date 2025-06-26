from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")
tools = toolbox.load_toolset('customerservice')

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='customer_service',
    description='Find customer information by searching by phone number or email and search their orders',
    instruction='Answer questions about user orders that can be searched by email or phone number ',
    tools=tools,
)
