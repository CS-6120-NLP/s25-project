# nodes/iteration_node.py

def iteration_node(query_data):
    """
    Iteration Node: Refine the query (e.g., through clarifications).
    For demonstration, append a marker.
    """
    query_data["normalized"] += " [refined]"
    return query_data
