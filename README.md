# cs6120-s25-project

## Overview

This project is part of CS 6120 for Spring 2025 and aims to build a Retrieval-Augmented Generation (RAG) based chatbot. The system is designed to answer academic and administrative questions for both students and staff at a university by combining document retrieval with language model generation.

## Project Structure
```
cs6120-s25-project/
├── models/
│   ├── __init__.py
│   └── entities.py
├── nodes/
│   ├── __init__.py
│   ├── access_guard_node.py
│   ├── agentic_ai_orchestrator_node.py
│   ├── confidence_assessment_node.py
│   ├── decision_node.py
│   ├── domain_specific_generation_node.py
│   ├── fallback_node.py
│   ├── final_answer_node.py
│   ├── input_node.py
│   ├── iteration_node.py
│   ├── logging_node.py
│   ├── output_node.py
│   ├── past_responses_lookup_node.py
│   ├── processing_node.py
│   ├── rag_node.py
│   └── semantic_classification_node.py
├── .gitignore
├── README.md
└── main.py
```

## How to Run

1. Clone the repository:
    `git clone [REPO]`
2. Navigate to the project directory:
    `cd cs6120-s25-project`
3. Run the main pipeline:
    `python main.py`

## Future Work

- Integrate real embedding and generative models.
- Expand the data ingestion pipeline.
- Enhance agentic decision-making logic.
- Add testing and continuous integration.

## License

[Specify your license here]
