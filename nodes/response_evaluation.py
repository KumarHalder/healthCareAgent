"""Response Evaluation Node - Phase 6 of HealthBot Workflow

This module handles collecting and evaluating patient answers to quiz questions,
providing feedback and citations.
"""
from states.health_bot_state import HealthBotState


def response_evaluation_node(state: HealthBotState) -> HealthBotState:
    """
    Collect patient answer, evaluate it, and provide feedback
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with evaluation results and feedback
    """
    try:
        # Get patient's answer
        patient_answer = input("💬 Your answer (A, B, C, or D): ").strip().upper()
        
        if patient_answer not in ['A', 'B', 'C', 'D']:
            print("⚠️ Please enter A, B, C, or D")
            return state
        
        state["patient_answer"] = patient_answer
        correct_answer = state["correct_answer"].upper()
        
        # Evaluate the response
        if patient_answer == correct_answer:
            grade = "✅ CORRECT!"
            print(f"\n🎉 {grade}")
        else:
            grade = "❌ INCORRECT"
            print(f"\n😔 {grade}")
            print(f"The correct answer was: {correct_answer}")
        
        state["grade"] = grade
        
        # Provide detailed explanation with citations
        print("\n" + "=" * 60)
        print("📝 EXPLANATION")
        print("=" * 60)
        print(f"\n{state['explanation']}")
        
        # Add citations from sources
        if state["information_sources"]:
            print(f"\n📚 This information was gathered from {len(state['information_sources'])} reliable medical sources:")
            for i, source in enumerate(state["information_sources"][:3], 1):  # Show top 3 sources
                print(f"   {i}. {source}")
        
        print("\n" + "=" * 60)
        
        state["current_phase"] = "session_management"
        
    except Exception as e:
        state["error_message"] = f"Error during response evaluation: {str(e)}"
        print(f"❌ Evaluation error: {e}")
    
    return state
