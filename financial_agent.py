from phi.agent import Agent, RunResponse
from phi.model.google import Gemini
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os 
from dotenv import load_dotenv
load_dotenv()



## web search agent
web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[DuckDuckGo()],
    instructions=["Alway include sources"],
    show_tools_calls=True,
    markdown=True,

)

## Financial agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Gemini(id="gemini-2.0-flash-exp"),
    instructions=["Always include sources", "Use tables to display the data  "],
    show_tool_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for APPLE", stream=True)
