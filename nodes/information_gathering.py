"""Information Gathering Node - Phase 2 of HealthBot Workflow

This module handles searching for relevant medical information using the web search tool.
"""
from states.health_bot_state import HealthBotState
from tools.config import get_tool_llm, tool_map
from langchain_core.output_parsers.openai_tools import parse_tool_calls
from langchain_core.messages import (
    HumanMessage, 
    SystemMessage, 
    ToolMessage
)


def information_gathering_node(state: HealthBotState) -> HealthBotState:
    """
    Use web search tool to find relevant, up-to-date medical information
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with search results and sources
    """
    # Add debug message to trace node execution
    node_message = {
        "type": "system", 
        "node": "information_gathering", 
        "phase": "2",
        "action": "starting_web_search",
        "topic": state["health_topic"]
    }
    state["messages"].append(node_message)
    
    try:
        health_topic = state["health_topic"]
        
        print(f"🔍 Searching for medical information about: {health_topic}")
        
        # Use tool-bound LLM to search for medical information with proper tool execution
        messages = [
            SystemMessage(content=
                          "Use the web_search tool to search for comprehensive medical information. Once you get the search results, use the structured data to provide detailed information. " \
                          "Use only the provided web_search tool results. If something is not present, state 'not found in results', summarize and result should not exceed 3-4 paragraphs."),
            HumanMessage(content=f"Find comprehensive medical information about {health_topic} including symptoms, causes, treatment, and prevention.")
        ]
        
        tool_llm = get_tool_llm()
        print(f"📤 Sending search request for: {health_topic}")
        
        # Get initial response with tool calls
        response = tool_llm.invoke(messages)
        messages.append(response)
        
        # Parse tool calls and execute them
        parsed_tool_calls_response = parse_tool_calls(
            response.additional_kwargs.get("tool_calls", [])
        )
        
        search_results = []
        sources = []
        
        for tool_call in parsed_tool_calls_response:
            tool_call_id = tool_call['id']
            function_name = tool_call['name']
            arguments = tool_call['args']
            
            # Log tool call execution
            tool_call_message = {
                "type": "system", 
                "node": "information_gathering", 
                "action": "tool_call_executed",
                "tool": function_name,
                "arguments": arguments,
                "tool_call_id": tool_call_id
            }
            state["messages"].append(tool_call_message)
            
            if function_name == 'web_search':
                print(f"🚀 Executing {function_name} with args: {arguments}")
                func = tool_map[function_name]
                result = func.invoke(arguments)
                
                # Process structured results
                if isinstance(result, dict):
                    # Add the main answer as a search result
                    search_results.append({
                        'title': f'Medical Information: {health_topic}',
                        'content': result.get('answer', ''),
                        'url': 'web_search_answer',
                        'answer': result.get('answer', '')
                    })
                    
                    # Add individual results with proper URLs
                    for search_item in result.get('results', []):
                        search_results.append({
                            'title': search_item.get('title', 'Search Result'),
                            'content': search_item.get('content', ''),
                            'url': search_item.get('url', ''),
                            'answer': search_item.get('content', '')
                        })
                        
                        # Collect real URLs for sources
                        if search_item.get('url') and search_item['url'] != 'web_search_tool':
                            sources.append(search_item['url'])
                
                # Add tool result to conversation
                tool_message = ToolMessage(
                    content=str(result),
                    name=function_name,
                    tool_call_id=tool_call_id,
                )
                messages.append(tool_message)
        
        # Get final processed response from LLM
        final_response = tool_llm.invoke(messages)
        print(f"✅ Search completed for {health_topic}")
        
        # Log search results obtained
        search_results_message = {
            "type": "system",
            "node": "information_gathering", 
            "action": "search_results_obtained",
            "results_count": len(search_results),
            "sources_count": len(sources),
            "final_response_content": final_response.content[:200] + "..." if len(final_response.content) > 200 else final_response.content
        }
        state["messages"].append(search_results_message)
        
        # Fallback: if no structured results, use the final response content
        if not search_results:
            search_results = [{
                'title': f'Medical Information: {health_topic}',
                'content': final_response.content if hasattr(final_response, 'content') else str(final_response),
                'url': 'web_search_tool',
                'answer': final_response.content if hasattr(final_response, 'content') else str(final_response)
            }]
        
        if not search_results:
            state["error_message"] = "No search results found. Please try a different health topic."
            return state
            
        # Store results and sources
        state["search_results"] = search_results
        state["information_sources"] = sources
        state["current_phase"] = "information_processing"
        
        # Log successful completion
        completion_message = {
            "type": "system", 
            "node": "information_gathering", 
            "action": "search_completed_successfully",
            "results_stored": len(search_results),
            "sources_stored": len(sources),
            "next_phase": "information_processing"
        }
        state["messages"].append(completion_message)
        
        print(f"✅ Found {len(search_results)} relevant medical sources")
        print(f"🔗 Collected {len(sources)} source URLs")
        print("📚 Processing information to create patient-friendly summary...\n")
        
    except Exception as e:
        # Log error for debugging
        error_message = {
            "type": "system", 
            "node": "information_gathering", 
            "action": "error",
            "error_type": "search_failed",
            "error_details": str(e)
        }
        state["messages"].append(error_message)
        
        state["error_message"] = f"Error during information gathering: {str(e)}"
        print(f"❌ Search error: {e}")
        import traceback
        traceback.print_exc()
    
    return state
