# nodes/agentic_ai_orchestrator_node.py

from nodes.confidence_assessment_node import confidence_assessment_node
from nodes.domain_specific_generation_node import domain_specific_generation_node
from nodes.past_responses_lookup_node import past_responses_lookup_node
from nodes.rag_node import rag_node


def agentic_ai_orchestrator_node(query_data):
    """
    Agent Node: Dynamically select the best retrieval strategy.
    """
    cached = past_responses_lookup_node(query_data)
    if cached:
        return cached
    domain_response = domain_specific_generation_node(query_data)
    if confidence_assessment_node(domain_response):
        return domain_response
    return rag_node(query_data)
