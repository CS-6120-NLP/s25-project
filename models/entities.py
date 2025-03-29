# models/entities.py

class DummyEmbeddingModel:
    def encode(self, text):
        # In practice, replace with a real embedding generator (e.g., Sentence Transformers)
        return [hash(text) % 1000]


class DummyGenerativeModel:
    def generate(self, prompt):
        # In practice, replace with a call to an LLM (e.g., OpenAI GPT, HuggingFace models)
        return f"Generated answer for prompt: {prompt}"
