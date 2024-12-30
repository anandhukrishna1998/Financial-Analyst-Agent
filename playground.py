import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
import re
import time

# Load environment variables
load_dotenv()


# Define Agents
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=False,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
            historical_prices=True,
            technical_indicators=True
        ),
    ],
    instructions=[
        "Use tables to display the data.",
        "Include technical indicators and historical prices to highlight trends."
    ],
    show_tool_calls=False,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["Always include sources", "Include technical indicators and historical prices to highlight trends."],
    show_tool_calls=False,
    markdown=True,
)

# Streamlit UI
st.title("Multi-Functional AI Chatbot")

# Sidebar for agent selection
st.sidebar.header("Settings")
agent_option = st.sidebar.selectbox(
    "Choose an agent:",
    ("Multi AI Agent", "Web Search Agent", "Finance AI Agent"),
)

# Input field for queries
user_input = st.text_input("Ask me anything (e.g., Stock analysis for TSLA, AAPL):")

# Select agent based on user choice
if agent_option == "Multi AI Agent":
    selected_agent = multi_ai_agent
elif agent_option == "Web Search Agent":
    selected_agent = web_search_agent
else:
    selected_agent = finance_agent

# Process response
if user_input:
    # Input sanitization
    safe_input = re.sub(r"[^a-zA-Z0-9 ]", "", user_input)
    with st.spinner("Processing your request..."):
        try:
            response = selected_agent.run(safe_input)
            if response and response.content:
                st.markdown(response.content)
            else:
                st.warning("No data found. Please refine your query.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Additional functionalities
st.sidebar.header("Additional Functionalities")

# Predefined stock list for dropdown
stock_list = ["AAPL", "TSLA", "GOOGL", "AMZN"]
stock_symbol = st.sidebar.selectbox("Select Stock Symbol", stock_list)

# Fetch Stock Data for Selected Symbol
if st.sidebar.button("Fetch Stock Data") and stock_symbol:
    with st.spinner(f"Fetching data for {stock_symbol}..."):
        try:
            response = finance_agent.run(f"Summarize analyst recommendations, share the latest news, and display candlestick patterns for {stock_symbol}")
            if response and response.content:
                st.markdown(response.content)
            else:
                st.warning(f"No data found for {stock_symbol}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Web Search Example
if st.sidebar.button("Search Latest Tech News"):
    with st.spinner("Searching the web..."):
        try:
            response = web_search_agent.run("Latest technology news")
            if response and response.content:
                st.markdown(response.content)
            else:
                st.warning("No tech news found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")



st.sidebar.markdown("---")
st.sidebar.markdown("Powered by Phi AI Agents")
