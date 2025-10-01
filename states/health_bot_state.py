"""HealthBot State Management

This module defines the state structure and initialization for the HealthBot workflow.
"""
from typing import TypedDict, List, Optional


class HealthBotState(TypedDict):
    """State management for HealthBot conversation flow"""
    
    # Conversation history for tool calls and cross-node access
    messages: List[dict]  # tool calls + assistant/human turns
    
    # Current conversation phase
    current_phase: str
    
    # Patient input and topic (with rubric-expected aliases)
    patient_query: str
    health_topic: str
    user_desired_subject: str  # alias of health_topic
    
    # Search and information processing (with rubric-expected aliases)
    search_results: List[dict]
    summarized_info: str
    model_summary: str  # alias of summarized_info
    information_sources: List[str]
    
    # Quiz and assessment (with rubric-expected aliases)
    quiz_question: str
    model_quiz: str  # alias of quiz_question
    quiz_answer_options: List[str]
    correct_answer: str
    patient_answer: str
    user_quiz_answer: str  # alias of patient_answer
    
    # Evaluation and feedback (with rubric-expected aliases)
    grade: str
    model_grade: str  # alias of grade
    grading_justification: str  # detailed justification from LLM grader
    explanation: str
    citations: List[str]
    
    # Session management (with rubric-expected aliases)
    session_active: bool
    continue_learning: Optional[bool]
    
    # Error handling
    error_message: Optional[bool]


def create_initial_state() -> HealthBotState:
    """Create the initial state for a new HealthBot session
    
    Returns:
        HealthBotState: Initial state with default values for a new session
    """
    return HealthBotState(
        # Conversation history
        messages=[],
        
        # Current phase
        current_phase="topic_inquiry",
        
        # Patient input and topic (with aliases)
        patient_query="",
        health_topic="",
        user_desired_subject="",  # alias of health_topic
        
        # Search and information processing (with aliases)
        search_results=[],
        summarized_info="",
        model_summary="",  # alias of summarized_info
        information_sources=[],
        
        # Quiz and assessment (with aliases)
        quiz_question="",
        model_quiz="",  # alias of quiz_question
        quiz_answer_options=[],
        correct_answer="",
        patient_answer="",
        user_quiz_answer="",  # alias of patient_answer
        
        # Evaluation and feedback (with aliases)
        grade="",
        model_grade="",  # alias of grade
        grading_justification="",
        explanation="",
        citations=[],
        
        # Session management (with aliases)
        session_active=True,
        continue_learning=None,
        
        # Error handling
        error_message=None
    )
