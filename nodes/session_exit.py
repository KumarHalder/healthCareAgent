"""Session Exit Node - Final phase of HealthBot Workflow

This module handles session cleanup and graceful exit.
The conditional logic for continuing vs exiting is now handled 
in the workflow_builder conditional edge.
"""
from states.health_bot_state import HealthBotState


def session_exit_node(state: HealthBotState) -> HealthBotState:
    """
    Handle session cleanup and graceful exit
    
    Note: This node is only reached when user has chosen to exit.
    The continue/exit decision is handled by the conditional edge 
    in workflow_builder.py
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Final state with session marked as complete
    """
    print("\n" + "=" * 60)
    print("🎯 HEALTHBOT SESSION ENDING")
    print("=" * 60)
    
    print("\n👋 Thank you for using HealthBot!")
    print("💙 Remember: This information is for educational purposes.")
    print("🏥 Always consult healthcare professionals for medical advice.")
    print("📚 Stay curious and keep learning about your health!")
    print("=" * 60)
    
    # Mark session as complete
    state["session_active"] = False
    state["continue_learning"] = False
    state["current_phase"] = "session_complete"
    
    return state


# Keep old function name for backward compatibility
def session_management_node(state: HealthBotState) -> HealthBotState:
    """
    Backward compatibility wrapper for session_exit_node
    """
    return session_exit_node(state)
