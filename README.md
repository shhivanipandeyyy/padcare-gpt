**Padcare GPT**


PadCare GPT is a lightweight AI assistant that answers questions about PadCare Labs using publicly available information. It supports internal teams by providing quick insights into PadCare’s mission, processes, and impact.



**Problem Overview**

PadCare Labs operates at the intersection of sustainability and sanitary waste management, where clarity and accuracy are critical. Internal teams frequently need quick, reliable information about PadCare’s work, purpose, and impact, but finding it often requires navigating multiple documents and sources.  With this project, I aim to build a focused AI assistant that serves as a single, reliable point of reference. It is designed to provide clear and accurate responses based strictly on publicly available information, while remaining fast, transparent, and dependable—without making assumptions or generating unsupported content.

**Solution Overview**

To address this gap, I am developing a focused AI assistant that acts as a single source of truth for PadCare Labs. It delivers fast, reliable answers grounded in public information, with a strong emphasis on accuracy, transparency, and avoiding hallucinations.

The application supports common internal requests, including:

Explaining the problem PadCare is addressing

Describing how PadCare’s recycling process works

Creating a short investor-focused pitch

Drafting LinkedIn content highlighting PadCare’s impact

Summarising PadCare’s work in clear, concise bullet points


**How It Works**

**Text Source**
All information comes from data/raw.txt, which contains publicly available details about PadCare Labs. No private or paid data is used.

**Chunking & Embeddings**
The text is split into smaller chunks to make it easier to search. Each chunk is converted into a vector embedding using all-MiniLM-L6-v2, which helps the system understand the meaning of each chunk.

**FAISS Vector Search**
A FAISS index is built from the embeddings. When you ask a question, the system quickly finds the most relevant chunks from the index.

**Answer Generation**
The system uses GPT-2, a causal language model, to generate natural, readable answers based strictly on the retrieved chunks. This ensures responses are factual, clear, and human-friendly.

**Interactive Q&A**
You can run the system locally or use the Streamlit app to type questions and receive answers instantly. It’s designed to be approachable, professional, and easy to use



**Key Features**

I ensure the assistant provides clear, human-readable answers in complete sentences. It avoids unnecessary repetition and is capable of handling simple questions, summaries, and generating basic posts or pitches. All responses are strictly grounded in carefully curated information.


**Tech Stack**

Python (google Collab)
Streamlit (for UI)
Text-based Knowledge Store
Prompt-driven AI logic (no paid APIs)


**Data Sources**

**data/raw.txt** containing publicly available information about PadCare Labs. (All information comes from the data/raw.txt file in this project.)

No private or paid data is used.
I do not use any private or paid data sources.

**Side Note**: The raw.txt file contains all the information about PadCare Labs that our system uses to answer questions. By storing the content in a single text file:

Centralised Knowledge – All relevant data is in one place, making it easier to update or expand.

Controlled Outputs – The language model only generates answers based on this file, preventing misinformation or hallucinations.

Simple & Transparent – Anyone can see exactly what the system knows, ensuring clarity and reproducibility


**Improvements with more time**

Add more sources to make answers richer.

Improve answer creativity and fluency.

Build a hosted demo online for easy access.

Add summarisation, bullet points, and LinkedIn pitch features for different types of outputs.

Add multilingual support




**Try It Yourself on Google Colab**

I’ve made a live Colab demo so you can explore PadCare GPT without installing anything. This notebook runs the full pipeline: it reads the raw text, creates embeddings, searches with FAISS, and generates answers with the language model. I put the Padcare_GPT_Assignment html
