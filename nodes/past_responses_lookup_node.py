# nodes/past_responses_lookup_node.py

def past_responses_lookup_node(query_data):
    """
    Retrieval Node: Lookup cached responses using normalization and ANN search.
    For demonstration, if the query contains "final exam", return a cached response.
    """
    if "final exam" in query_data["normalized"]:
        return "Final exam dates for Spring 2025: [Dates here]"
    return None
