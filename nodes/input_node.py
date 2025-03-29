# nodes/input_node.py

def input_node(raw_query, user_metadata):
    """
    Input Node: Capture raw query and user metadata.
    """
    return {"original": raw_query, "normalized": raw_query.lower().strip(), "metadata": user_metadata}
