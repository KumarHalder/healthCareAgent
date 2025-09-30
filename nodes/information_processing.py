"""Information Processing Node - Phase 3 of HealthBot Workflow

This module handles processing and summarizing search results into patient-friendly language
using the AI language model.
"""
from langchain.schema import HumanMessage
from states.health_bot_state import HealthBotState
from tools.config import get_llm


def information_processing_node(state: HealthBotState) -> HealthBotState:
    """
    Summarize search results into patient-friendly language
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with summarized information
    """
    try:
        search_results = state["search_results"]
        health_topic = state["health_topic"]
        
        # Combine search results content
        combined_content = ""
        for result in search_results:
            if 'content' in result:
                combined_content += result['content'] + "\n\n"
            elif 'answer' in result:
                combined_content += result['answer'] + "\n\n"
        
        # Create summarization prompt
        summarization_prompt = f"""
        You are a healthcare educator. Create a clear, patient-friendly summary about {health_topic}.
        
        Use this medical information:
        {combined_content}

        Please Summarize only the provided content into 3-4 paragraphs. Do not use outside knowledge.
        """
        
        print("🧠 Creating patient-friendly summary using AI...")
        
        # Get LLM and generate summary
        llm = get_llm()
        response = llm.invoke([HumanMessage(content=summarization_prompt)])
        
        state["summarized_info"] = response.content
        state["current_phase"] = "information_presentation"
        
        print("✅ Medical information processed into patient-friendly format")
        
    except Exception as e:
        state["error_message"] = f"Error during information processing: {str(e)}"
        print(f"❌ Processing error: {e}")
    
    return state
