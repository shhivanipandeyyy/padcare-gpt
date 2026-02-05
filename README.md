Padcare GPT

PadCare GPT is a lightweight AI assistant that answers questions about PadCare Labs using publicly available information. It supports internal teams by providing quick insights into PadCare’s mission, processes, and impact.



Problem Overview

PadCare Labs operates at the intersection of sustainability and sanitary waste management, where clarity and accuracy are critical. Internal teams frequently need quick, reliable information about PadCare’s work, purpose, and impact, but finding it often requires navigating multiple documents and sources.  With this project, I aim to build a focused AI assistant that serves as a single, reliable point of reference. It is designed to provide clear and accurate responses based strictly on publicly available information, while remaining fast, transparent, and dependable—without making assumptions or generating unsupported content.

Solution Overview

To address this gap, I am developing a focused AI assistant that acts as a single source of truth for PadCare Labs. It delivers fast, reliable answers grounded in public information, with a strong emphasis on accuracy, transparency, and avoiding hallucinations.

The application supports common internal requests, including:

Explaining the problem PadCare is addressing

Describing how PadCare’s recycling process works

Creating a short investor-focused pitch

Drafting LinkedIn content highlighting PadCare’s impact

Summarising PadCare’s work in clear, concise bullet points


How It Works

The system reads the text in data/raw.txt (publicly available information about PadCare).

It splits the text into small chunks and creates embeddings using a sentence transformer.

A FAISS vector index is built to quickly find relevant chunks for any question.

A language model (Flan-T5) generates answers based only on these chunks.

The app can be used locally or through Streamlit for a friendly Q&A interface.
The application processes each query using keyword-driven prompt logic to identify relevant context. Based on this, it generates a clear and structured response drawn strictly from the stored knowledge. Safeguards are built in to ensure the outputs remain factual, controlled, and free from assumptions or hallucinated information.


Tech Stack

Python (google Collab)
Streamlit (for UI)
Text-based Knowledge Store
Prompt-driven AI logic (no paid APIs)


Data Sources

data/raw.txt containing publicly available information about PadCare Labs.

No private or paid data is used.
I do not use any private or paid data sources.


Improvements with more time

Add more sources to make answers richer.

Improve answer creativity and fluency.

Build a hosted demo online for easy access.

Add summarisation, bullet points, and LinkedIn pitch features for different types of outputs.
