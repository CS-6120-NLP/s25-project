# nodes/domain_specific_generation_node.py

from models.entities import DummyGenerativeModel

generative_model = DummyGenerativeModel()


def domain_specific_generation_node(query_data):
    """
    LLM Node: Generate answer using a domain-specific fine-tuned model.
    """
    prompt = f"Generate answer for: {query_data['normalized']}"
    return generative_model.generate(prompt)
