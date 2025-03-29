# nodes/fallback_node.py

def fallback_node(query_data):
    """
    Fallback Node: Provide a fallback response if the query is disallowed or the answer is low confidence.
    """
    return f"Your query '{query_data['original']}' requires further assistance. Please contact support."
