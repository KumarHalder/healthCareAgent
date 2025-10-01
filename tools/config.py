"""Tools configuration for HealthBot

This module provides centralized access to all tools used in the HealthBot workflow.
"""
import os
from langchain_openai import ChatOpenAI
from tools.web_search import web_search


def get_llm():
    """Get the configured LLM instance"""
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        max_tokens=1000,
        base_url="https://openai.vocareum.com/v1",
        api_key=os.getenv('OPENAI_API_KEY')
    )


def get_tool_llm():
    """Get LLM with web_search tool bound to it"""
    llm = get_llm()
    return llm.bind_tools(tools)


def get_search_tool():
    """Get the web search tool"""
    return web_search


# Tool registry for easy access
tools = [web_search]
tool_map = {tool.name: tool for tool in tools}
