"""Response Evaluation Node - Phase 6 of HealthBot Workflow

This module handles collecting and        # Add citations         # Add citations from sources
        if state["information_sources"]:
            print(f"\n🔗 This information was gathered from {len(state['information_sources'])} reliable medical sources:")
            for i, source in enumerate(state["information_sources"][:3], 1):  # Show top 3 sources
                print(f"   {i}. {source}")
        
        print("\n" + "=" * 60)
        
        # Ask user if they want to continue learning (conditional anchor)
        print("🎯 LEARNING SESSION COMPLETE!")
        continue_choice = input("\n🤔 Would you like to learn about another health topic? (yes/no): ").strip().lower()
        
        # Update continue_learning field that controls the conditional edge
        if continue_choice in ['yes', 'y', 'yeah', 'sure', 'ok', 'okay', '1']:
            state["continue_learning"] = True
            print("\n🔄 Great! Let's learn about another topic...")
        else:
            state["continue_learning"] = False
            print("\n👋 Thank you for learning with HealthBot!")
        
        # Update state aliases for consistency
        state["model_grade"] = grade  # Alias for rubric compliance
        state["user_quiz_answer"] = patient_answer  # Alias for rubric compliance
        state["current_phase"] = "conditional_check"  # Ready for conditional edgeces
        if state["information_sources"]:
            print(f"\n🔗 This information was gathered from {len(state['information_sources'])} reliable medical sources:")
            for i, source in enumerate(state["information_sources"][:3], 1):  # Show top 3 sources
                print(f"   {i}. {source}")
        
        print("\n" + "=" * 60)
        
        # Ask user if they want to continue learning (conditional anchor)
        # Note: User continuation prompt is handled at the end of the function
providing feedback and citations.
"""
from langchain.schema import HumanMessage
from states.health_bot_state import HealthBotState
from tools.config import get_llm


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
        
        # Create grading prompt that follows the specified contract
        grade_prompt = f"""
        Grade the patient's answer based ONLY on the information in the model summary below.
        
        Model Summary:
        {state['summarized_info']}
        
        Patient Answer: {patient_answer}
        
        Quiz Question: {state['quiz_question']}
        Answer Options:
        {chr(10).join(state['quiz_answer_options'])}
        
        GRADING INSTRUCTIONS:
        - Output (a) grade (A-D) and (b) justification that quotes/paraphrases exact lines from model_summary
        - Grade A: Completely correct based on model summary
        - Grade B: Mostly correct with minor gaps
        - Grade C: Partially correct but missing key points
        - Grade D: Incorrect or contradicts model summary
        
        Format your response EXACTLY as follows:
        GRADE: [A, B, C, or D]
        JUSTIFICATION: [Quote or paraphrase exact lines from the model summary that support this grade]
        
        Example format:
        GRADE: A
        JUSTIFICATION: According to the model summary, "diabetes is characterized by high blood sugar levels," which directly supports the patient's correct identification of this key symptom.
        """
        
        print("\n� Evaluating your answer...")
        
        # Get LLM-based grading
        llm = get_llm()
        response = llm.invoke([HumanMessage(content=grade_prompt)])
        grading_result = response.content
        
        # Parse the grading result
        lines = grading_result.split('\n')
        grade = ""
        justification = ""
        
        for line in lines:
            line = line.strip()
            if line.startswith("GRADE:"):
                grade = line.replace("GRADE:", "").strip()
            elif line.startswith("JUSTIFICATION:"):
                justification = line.replace("JUSTIFICATION:", "").strip()
        
        state["grade"] = grade
        state["grading_justification"] = justification
        
        # Display results
        grade_display = {
            'A': "✅ EXCELLENT!",
            'B': "👍 GOOD!",
            'C': "⚠️ PARTIAL",
            'D': "❌ INCORRECT"
        }
        
        print(f"\n🎯 GRADE: {grade_display.get(grade, grade)}")
        print(f"📝 JUSTIFICATION: {justification}")
        
        
        # Provide additional explanation if available
        if state.get('explanation'):
            print(f"\n� ADDITIONAL CONTEXT: {state['explanation']}")
        
        # Add citations from sources
        if state["information_sources"]:
            print(f"\n� This information was gathered from {len(state['information_sources'])} reliable medical sources:")
            for i, source in enumerate(state["information_sources"][:3], 1):  # Show top 3 sources
                print(f"   {i}. {source}")
        
        print("\n" + "=" * 60)
        
        # Ask user if they want to continue learning
        print("\n🤔 Would you like to learn about another health topic?")
        continue_choice = input("💬 Enter 'yes' to learn more or 'no' to exit: ").strip().lower()
        
        if continue_choice in ['yes', 'y', '1', 'true', 'continue']:
            state["continue_learning"] = True
            print("\n🔄 Great! Let's learn about another topic...")
        else:
            state["continue_learning"] = False
            print("\n👋 Thank you for learning with HealthBot!")
        
        # Update state aliases for consistency
        state["model_grade"] = grade  # Alias for rubric compliance
        state["current_phase"] = "conditional_check"  # Ready for conditional edge
        
    except Exception as e:
        state["error_message"] = f"Error during response evaluation: {str(e)}"
        print(f"❌ Evaluation error: {e}")
    
    return state
