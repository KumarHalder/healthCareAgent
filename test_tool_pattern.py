"""Test script to demonstrate the new tool-bound LLM pattern"""
import os
from tools.config import get_tool_llm

# Make sure you have your API keys set
if not os.getenv('OPENAI_API_KEY'):
    print("Please set OPENAI_API_KEY environment variable")
    exit(1)

if not os.getenv('TAVILY_API_KEY'):
    print("Please set TAVILY_API_KEY environment variable")
    exit(1)

# Test the tool-bound LLM pattern
def test_tool_pattern():
    print("Testing tool-bound LLM pattern...")
    
    # Get the tool-bound LLM
    tool_llm = get_tool_llm()
    
    # Test query similar to your example
    response = tool_llm.invoke("Use web_search to find 2 key facts about aspirin.")
    
    print("Response:")
    print(response.content if hasattr(response, 'content') else str(response))
    
    # Test with a medical query
    print("\n" + "="*50)
    print("Testing with medical query...")
    
    medical_response = tool_llm.invoke("Use web_search to find information about diabetes symptoms and treatment.")
    
    print("Medical Response:")
    print(medical_response.content if hasattr(medical_response, 'content') else str(medical_response))

if __name__ == "__main__":
    test_tool_pattern()