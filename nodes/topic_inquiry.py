"""Topic Inquiry Node - Phase 1 of HealthBot Workflow

This module handles the initial patient interaction to gather the health topic
they want to learn about.
"""
from states.health_bot_state import HealthBotState


def topic_inquiry_node(state: HealthBotState) -> HealthBotState:
    """
    Ask the patient what health topic they'd like to learn about
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with patient query and health topic
    """
    print("=" * 60)
    print("🏥 Welcome to HealthBot - Your AI Health Education Assistant!")
    print("=" * 60)
    print("\nI'm here to help you learn about health topics in a friendly,")
    print("easy-to-understand way. After providing information, I'll test")
    print("your understanding with a simple quiz question.\n")
    
    # Get patient input
    patient_query = input("💬 What health topic or medical condition would you like to learn about? ")
    
    if not patient_query.strip():
        state["error_message"] = "Please provide a health topic to learn about."
        return state
    
    # Process and validate the query
    state["patient_query"] = patient_query.strip()
    state["health_topic"] = patient_query.strip()
    state["current_phase"] = "information_gathering"
    state["error_message"] = None
    
    print(f"\n✅ Great! I'll help you learn about: {state['health_topic']}")
    print("🔍 Let me search for the most current and reliable information...\n")
    
    return state
