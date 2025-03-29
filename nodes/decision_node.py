# nodes/decision_node.py

def decision_node_high_confidence(classification, threshold=0.8):
    """
    Decision Node: Check if classification confidence is high.
    """
    return classification.get("confidence", 0) >= threshold


def decision_node_query_allowed(query_data):
    """
    Decision Node: Check if the query is allowed (role-based access, etc.).
    """
    return query_data.get("access_allowed", False)
