# nodes/access_guard_node.py

def access_guard_node(query_data):
    """
    Processing Node: Evaluate query against role-based access.
    For now, assume all queries are allowed.
    """
    query_data["access_allowed"] = True
    return query_data
