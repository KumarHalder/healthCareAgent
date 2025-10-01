"""Comprehension Assessment Node - Phase 5 of HealthBot Workflow

This module handles generating and presenting quiz questions to assess
patient understanding of the health information.
"""
from langchain.schema import HumanMessage
from states.health_bot_state import HealthBotState
from tools.config import get_llm


def comprehension_assessment_node(state: HealthBotState) -> HealthBotState:
    """
    Generate a relevant quiz question based on the provided information
    
    Args:
        state: Current HealthBot state
        
    Returns:
        HealthBotState: Updated state with quiz question and options
    """
    try:
        summarized_info = state["summarized_info"]
        health_topic = state["health_topic"]
        
        # Create quiz generation prompt
        quiz_prompt = f"""
        Frame one question whose answer is verbatim inferable from this summary. Do not require knowledge not contained in the summary.
        
        Model Summary:
        {summarized_info}
        
        INSTRUCTIONS:
        - Create a single multiple-choice question that tests patient understanding
        - The question and correct answer must be verbatim inferable from the provided summary
        - All answer options (correct and incorrect) must reference only information from the summary
        - Do not include any information not explicitly mentioned in the summary
        - Focus on key facts that are directly stated in the summary content
        
        Format your response as:
        QUESTION: [Your question here]
        A) [Option A]
        B) [Option B] 
        C) [Option C]
        D) [Option D]
        CORRECT: [Letter of correct answer]
        EXPLANATION: [Brief explanation using only information from the summary]
        """
        
        print("🧠 Generating comprehension question...")
        
        # Get LLM and generate quiz
        llm = get_llm()
        response = llm.invoke([HumanMessage(content=quiz_prompt)])
        quiz_content = response.content
        
        # Parse the response to extract components
        lines = quiz_content.split('\n')
        question = ""
        options = []
        correct_answer = ""
        explanation = ""
        
        for line in lines:
            line = line.strip()
            if line.startswith("QUESTION:"):
                question = line.replace("QUESTION:", "").strip()
            elif line.startswith(("A)", "B)", "C)", "D)")):
                options.append(line)
            elif line.startswith("CORRECT:"):
                correct_answer = line.replace("CORRECT:", "").strip()
            elif line.startswith("EXPLANATION:"):
                explanation = line.replace("EXPLANATION:", "").strip()
        
        # Store quiz information
        state["quiz_question"] = question
        state["quiz_answer_options"] = options
        state["correct_answer"] = correct_answer
        state["explanation"] = explanation
        state["current_phase"] = "response_collection"
        
        # Present the quiz question
        print("=" * 60)
        print("🧪 COMPREHENSION CHECK")
        print("=" * 60)
        print(f"\n❓ {question}\n")
        
        for option in options:
            print(f"   {option}")
        
        print("\n" + "=" * 60)
        
    except Exception as e:
        state["error_message"] = f"Error during quiz generation: {str(e)}"
        print(f"❌ Quiz generation error: {e}")
    
    return state
