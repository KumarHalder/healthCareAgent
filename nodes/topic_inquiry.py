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
    # Add debug message to trace node execution
    node_message = {
        "type": "system", 
        "node": "topic_inquiry", 
        "phase": "1",
        "timestamp": "workflow_start",
        "action": "requesting_health_topic"
    }
    state["messages"].append(node_message)
    
    # Check if this is a returning user (loop back)
    is_returning = state.get("continue_learning") == True
    
    if is_returning:
        print("\n" + "=" * 60)
        print("🔄 NEW LEARNING TOPIC")
        print("=" * 60)
        print("📝 Starting fresh for privacy and accuracy...")
        
        # Add debug message for returning user
        returning_message = {
            "type": "system", 
            "node": "topic_inquiry", 
            "action": "returning_user_reset",
            "details": "resetting state for new topic"
        }
        state["messages"].append(returning_message)
        
        # Reset topic-specific fields for new learning session
        state["patient_query"] = ""
        state["health_topic"] = ""
        state["user_desired_subject"] = ""
        state["search_results"] = []
        state["summarized_info"] = ""
        state["model_summary"] = ""
        state["information_sources"] = []
        state["quiz_question"] = ""
        state["model_quiz"] = ""
        state["quiz_answer_options"] = []
        state["correct_answer"] = ""
        state["patient_answer"] = ""
        state["user_quiz_answer"] = ""
        state["grade"] = ""
        state["model_grade"] = ""
        state["grading_justification"] = ""
        state["explanation"] = ""
        state["citations"] = []
        state["error_message"] = None
        
        # Reset continuation flag
        state["continue_learning"] = None
    else:
        print("=" * 60)
        print("🏥 Welcome to HealthBot - Your AI Health Education Assistant!")
        print("=" * 60)
        print("\nI'm here to help you learn about health topics in a friendly,")
        print("easy-to-understand way. After providing information, I'll test")
        print("your understanding with a simple quiz question.\n")
    
    # Get patient input
    patient_query = input("💬 What health topic or medical condition would you like to learn about? ")
    
    # Log user input for debugging
    user_input_message = {
        "type": "human", 
        "node": "topic_inquiry", 
        "content": patient_query,
        "action": "topic_selection"
    }
    state["messages"].append(user_input_message)
    
    if not patient_query.strip():
        error_message = {
            "type": "system", 
            "node": "topic_inquiry", 
            "action": "error",
            "details": "empty_topic_provided"
        }
        state["messages"].append(error_message)
        state["error_message"] = "Please provide a health topic to learn about."
        return state
    
    # Process and validate the query
    state["patient_query"] = patient_query.strip()
    state["health_topic"] = patient_query.strip()
    state["user_desired_subject"] = patient_query.strip()  # Rubric alias
    state["current_phase"] = "information_gathering"
    state["error_message"] = None
    
    # Log successful topic capture
    success_message = {
        "type": "system", 
        "node": "topic_inquiry", 
        "action": "topic_captured",
        "topic": state["health_topic"],
        "next_phase": "information_gathering"
    }
    state["messages"].append(success_message)
    
    print(f"\n✅ Great! I'll help you learn about: {state['health_topic']}")
    print("🔍 Let me search for the most current and reliable information...\n")
    
    return state
