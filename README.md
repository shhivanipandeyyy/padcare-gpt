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

I curate and maintain publicly available information about PadCare in a structured, text-based knowledge file. Users interact with the system through a simple Streamlit interface, where they can submit their questions.

The application processes each query using keyword-driven prompt logic to identify relevant context. Based on this, it generates a clear and structured response drawn strictly from the stored knowledge. Safeguards are built in to ensure the outputs remain factual, controlled, and free from assumptions or hallucinated information.


Tech Stack

Python
Streamlit (for UI)
Text-based Knowledge Store
Prompt-driven AI logic (no paid APIs)


Data Sources

I curate information from publicly accessible sources such as PadCare Labs’ website, public reports, and verified online content. The system is designed to use only this curated material to ensure accuracy and transparency.
I do not use any private or paid data sources.
