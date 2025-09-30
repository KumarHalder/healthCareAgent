"""Information Presentation Node - Phase 4 of HealthBot Workflow

This module handles presenting the summarized health information to the patient
in a clear and structured format.
"""
from states.health_bot_state import HealthBotState


def information_presentation_node(state: HealthBotState) -> HealthBotState:
    """
    Present the summarized information to the patient
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state ready for comprehension assessment
    """
    print("=" * 60)
    print(f"📚 HEALTH INFORMATION: {state['health_topic'].upper()}")
    print("=" * 60)
    
    # Present the summarized information
    print(state["summarized_info"])
    
    print("\n" + "=" * 60)
    print("📖 Please take your time to read and understand this information.")
    print("When you're ready, I'll ask you a question to check your understanding.")
    print("=" * 60)
    
    # Wait for patient confirmation
    ready = input("\n✅ Press Enter when you're ready for the comprehension check... ")
    
    state["current_phase"] = "comprehension_assessment"
    
    print("\n🧪 Generating a comprehension question based on the information...\n")
    
    return state
