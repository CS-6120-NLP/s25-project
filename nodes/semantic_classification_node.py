# nodes/semantic_classification_node.py

def semantic_classification_node(query_data):
    """
    LLM Node: Perform initial semantic classification.
    Here, we use a dummy method based on query length.
    """
    confidence = 0.9 if len(query_data["normalized"]) > 5 else 0.5
    return {"label": "general", "confidence": confidence}
