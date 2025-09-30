"""Information Gathering Node - Phase 2 of HealthBot Workflow

This module handles searching for relevant medical information using the web search tool.
"""
from states.health_bot_state import HealthBotState
from tools.config import get_tool_llm


def information_gathering_node(state: HealthBotState) -> HealthBotState:
    """
    Use web search tool to find relevant, up-to-date medical information
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with search results and sources
    """
    try:
        health_topic = state["health_topic"]
        
        print(f"🔍 Searching for medical information about: {health_topic}")
        
        # Use tool-bound LLM to search for medical information
        tool_llm = get_tool_llm()
        prompt = f"Use web_search to find comprehensive medical information about {health_topic} including symptoms, causes, treatment, and prevention."
        response = tool_llm.invoke(prompt)
        
        # Extract the search result from the response
        search_result = response.content if hasattr(response, 'content') else str(response)
        
        # Convert to expected format
        if isinstance(search_result, str):
            search_results = [{
                'title': 'Search Results',
                'content': search_result,
                'url': 'web_search_tool',
                'answer': search_result
            }]
        else:
            search_results = search_result if search_result else []
        
        if not search_results:
            state["error_message"] = "No search results found. Please try a different health topic."
            return state
            
        # Store results and extract sources
        state["search_results"] = search_results
        sources = []
        
        for result in search_results:
            if 'url' in result and result['url'] != 'web_search_tool':
                sources.append(result['url'])
        
        state["information_sources"] = sources
        state["current_phase"] = "information_processing"
        
        print(f"✅ Found {len(search_results)} relevant medical sources")
        print("📚 Processing information to create patient-friendly summary...\n")
        
    except Exception as e:
        state["error_message"] = f"Error during information gathering: {str(e)}"
        print(f"❌ Search error: {e}")
    
    return state
