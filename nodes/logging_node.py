# nodes/logging_node.py

def logging_node(query_data, answer, user_feedback=None):
    """
    Logging Node: Log the interaction for feedback and continuous improvement.
    """
    print("Logging Interaction:")
    print(f"Query: {query_data['original']}")
    print(f"Answer: {answer}")
    if user_feedback:
        print(f"User Feedback: {user_feedback}")
