# nodes/rag_node.py

from models.entities import DummyGenerativeModel

generative_model = DummyGenerativeModel()


def rag_node(query_data):
    """
    Retrieval Node: Perform Retrieval-Augmented Generation (RAG).
    """
    retrieved_context = "Relevant university document snippets."
    prompt = f"Query: {query_data['normalized']}\nContext: {retrieved_context}\nAnswer:"
    return generative_model.generate(prompt)
