"""Session Management Node - Phase 7 of HealthBot Workflow

This module handles session continuation decisions and state management
for new learning sessions or session completion.
"""
from states.health_bot_state import HealthBotState, create_initial_state


def session_management_node(state: HealthBotState) -> HealthBotState:
    """
    Ask if patient wants to learn about another topic or exit
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: New state for next session or completed state for exit
    """
    print("\n" + "=" * 60)
    print("🎯 LEARNING SESSION COMPLETE!")
    print("=" * 60)
    
    # Ask about continuing
    continue_choice = input("\n🤔 Would you like to learn about another health topic? (yes/no): ").strip().lower()
    
    if continue_choice in ['yes', 'y', 'yeah', 'sure', 'ok', 'okay']:
        print("\n🔄 Starting a new learning session...")
        print("📝 Resetting for privacy and accuracy...\n")
        
        # Reset state for new topic (privacy and accuracy)
        new_state = create_initial_state()
        new_state["current_phase"] = "topic_inquiry"
        return new_state
        
    else:
        print("\n👋 Thank you for using HealthBot!")
        print("💙 Remember: This information is for educational purposes.")
        print("🏥 Always consult healthcare professionals for medical advice.")
        print("=" * 60)
        
        state["session_active"] = False
        state["continue_learning"] = False
        state["current_phase"] = "session_complete"
    
    return state
