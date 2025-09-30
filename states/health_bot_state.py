"""HealthBot State Management

This module defines the state structure and initialization for the HealthBot workflow.
"""
from typing import TypedDict, List, Optional


class HealthBotState(TypedDict):
    """State management for HealthBot conversation flow"""
    
    # Current conversation phase
    current_phase: str
    
    # Patient input and topic
    patient_query: str
    health_topic: str
    
    # Search and information processing
    search_results: List[dict]
    summarized_info: str
    information_sources: List[str]
    
    # Quiz and assessment
    quiz_question: str
    quiz_answer_options: List[str]
    correct_answer: str
    patient_answer: str
    
    # Evaluation and feedback
    grade: str
    explanation: str
    citations: List[str]
    
    # Session management
    session_active: bool
    continue_learning: Optional[bool]
    
    # Error handling
    error_message: Optional[str]


def create_initial_state() -> HealthBotState:
    """Create the initial state for a new HealthBot session
    
    Returns:
        HealthBotState: Initial state with default values for a new session
    """
    return HealthBotState(
        current_phase="topic_inquiry",
        patient_query="",
        health_topic="",
        search_results=[],
        summarized_info="",
        information_sources=[],
        quiz_question="",
        quiz_answer_options=[],
        correct_answer="",
        patient_answer="",
        grade="",
        explanation="",
        citations=[],
        session_active=True,
        continue_learning=None,
        error_message=None
    )
