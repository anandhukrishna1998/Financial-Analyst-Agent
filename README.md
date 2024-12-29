# Multi-Functional AI Agent Chatbot

This project consists of a Streamlit-based AI-powered chatbot that leverages multiple agents to perform web searches and provide financial data analysis using Yahoo Finance.

## Overview

The system is built around three main components:
1. **Web Search Agent** - Searches the web for relevant information and includes sources in the results.
2. **Finance AI Agent** - Provides detailed financial analysis, including stock data, analyst recommendations, company news, and technical indicators, using Yahoo Finance.
3. **Multi AI Agent** - A combination of both the Web Search and Finance AI Agents, designed to answer queries that require both web search results and financial analysis.

The chatbot allows users to interact with these agents in a seamless manner via a web interface built with Streamlit.

## Components

### 1. Web Search Agent
- This agent utilizes **Gemini** (Google model) to search the web for information and returns the results along with sources.
- It uses the **DuckDuckGo** search tool for querying the web.

### 2. Finance AI Agent
- This agent utilizes **Gemini** (Google model) for financial analysis.
- It integrates with **Yahoo Finance** tools to provide:
  - Stock prices
  - Analyst recommendations
  - Company fundamentals
  - Latest company news
  - Financial data analysis (e.g., historical prices, technical indicators)

### 3. Multi AI Agent
- Combines the capabilities of both the Web Search and Finance AI Agents to provide a comprehensive response to queries.
- Supports queries requiring both web search and financial data.

## Features

- **Agent Selection**: Users can select from the available agents (Web Search Agent, Finance AI Agent, or Multi AI Agent) through a sidebar interface.
- **Stock Data Fetching**: Users can input stock symbols (e.g., AAPL, TSLA) to get detailed stock analysis, including recommendations, news, and technical indicators.
- **Search Functionality**: Users can search the web for the latest news or any other queries.
- **Progress Bar**: A progress bar is included to show real-time processing during long queries.


