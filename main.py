# main.py

from nodes.access_guard_node import access_guard_node
from nodes.agentic_ai_orchestrator_node import agentic_ai_orchestrator_node
from nodes.confidence_assessment_node import confidence_assessment_node
from nodes.decision_node import decision_node_high_confidence, decision_node_query_allowed
from nodes.fallback_node import fallback_node
from nodes.final_answer_node import final_answer_node
from nodes.input_node import input_node
from nodes.iteration_node import iteration_node
from nodes.logging_node import logging_node
from nodes.output_node import output_node
from nodes.processing_node import processing_node
from nodes.semantic_classification_node import semantic_classification_node


def main_pipeline(raw_query, user_metadata):
    # Input Node: Capture raw query and metadata.
    query_data = input_node(raw_query, user_metadata)

    # Processing Node: Preprocess the query.
    query_data = processing_node(query_data)

    # LLM Node: Initial Semantic Classification.
    classification = semantic_classification_node(query_data)

    # Decision Node: Check if confidence is high.
    if not decision_node_high_confidence(classification):
        query_data = iteration_node(query_data)
        classification = semantic_classification_node(query_data)

    # Processing Node: Access Guard.
    query_data = access_guard_node(query_data)

    # Decision Node: Check if query is allowed.
    if not decision_node_query_allowed(query_data):
        answer = fallback_node(query_data)
        output_node(answer)
        logging_node(query_data, answer)
        return answer

    # Agent Node: Dynamically select the best retrieval strategy.
    answer = agentic_ai_orchestrator_node(query_data)

    # Evaluation Node: Assess answer confidence.
    if not confidence_assessment_node(answer):
        answer = fallback_node(query_data)

    # LLM Node: Final Answer Generation.
    final_answer = final_answer_node(answer)

    # Output Node: Present answer.
    output_node(final_answer)

    # Logging Node: Log the interaction.
    logging_node(query_data, final_answer)

    return final_answer


if __name__ == "__main__":
    raw_query = "What are the final exam dates for Spring 2025?"
    user_metadata = {
        "role": "student",
        "academic_term": "Spring 2025",
        "session_history": []
    }
    main_pipeline(raw_query, user_metadata)
