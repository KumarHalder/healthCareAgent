"""Web search tool using Tavily API."""
import os
from typing import Optional
from langchain_core.tools import tool
from tavily import TavilyClient

# Initialize Tavily client
tavily_client = TavilyClient(api_key=os.getenv('TAVILY_API_KEY'))

@tool("web_search")
def web_search(q: str) -> str:
    """Search for current medical and health information using Tavily.
    
    Args:
        q: The search query string
        
    Returns:
        str: The search results formatted as a string
    """
    try:
        response = tavily_client.search(q, search_depth="advanced", include_answer=True)
        return {
            "answer": response.get("answer"),
            "results": response.get("results", []),
        }
    except Exception as e:
        return f"Search error: {str(e)}"
