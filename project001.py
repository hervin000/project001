# src/search_workflow.py
from langgraph.graph import StateGraph, START, END
from .state import TopicState

def search_router_node(state: TopicState) -> dict:
    """Route to appropriate search based on topic type."""
    topics = state.get("topics", [])
    if not topics:
        return {"intent": "general"}
    
    topic_name = topics[0]["topic"].lower()
    
    if any(kw in topic_name for kw in ["finance", "market", "stock"]):
        return {"intent": "financial"}
    elif any(kw in topic_name for kw in ["medical", "health", "disease"]):
        return {"intent": "medical"}
    else:
        return {"intent": "general"}

def financial_search_node(state: TopicState) -> dict:
    """Execute financial domain search."""
    queries = state.get("search_queries", [])
    # Simulated search results
    results = [f"Financial result for: {q}" for q in queries[:2]]
    return {"retrieved_documents": results}

def medical_search_node(state: TopicState) -> dict:
    """Execute medical domain search."""
    queries = state.get("search_queries", [])
    results = [f"Medical result for: {q}" for q in queries[:2]]
    return {"retrieved_documents": results}

def general_search_node(state: TopicState) -> dict:
    """Execute general domain search."""
    queries = state.get("search_queries", [])
    results = [f"General result for: {q}" for q in queries[:2]]
    return {"retrieved_documents": results}