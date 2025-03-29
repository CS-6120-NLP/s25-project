# nodes/confidence_assessment_node.py

def confidence_assessment_node(answer):
    """
    Evaluation Node: Check if the answer meets a confidence threshold.
    For demonstration, any answer containing "Generated" is assumed to be high confidence.
    """
    return "Generated" in answer
