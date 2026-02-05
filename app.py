pip install streamlit transformers sentence-transformers faiss-cpu

# A simple Streamlit app for PadCare GPT
# Lets users ask questions about PadCare Labs and get human-like answers

import streamlit as st
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# -------------------------------
# Page setup
# -------------------------------
st.set_page_config(page_title="PadCare GPT", layout="centered")
st.title("PadCare GPT ")
st.markdown(
    "Ask anything about PadCare Labs and their work on sustainable menstrual waste management."
)

# -------------------------------
# Load models and data
# -------------------------------

# SentenceTransformer model for embedding questions
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# T5 model + tokenizer for generating natural answers
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

# FAISS index for fast retrieval of relevant text chunks
index = faiss.read_index("padcare_gpt/index/index.faiss")
chunks = pickle.load(open("padcare_gpt/index/chunks.pkl", "rb"))

# -------------------------------
# Function to handle chat
# -------------------------------
def padcare_chat(question):
    """
    Takes a user question, finds the most relevant text chunks, 
    and uses the T5 model to generate a natural answer.
    """
    # Turn question into embedding vector
    q_vec = embedder.encode([question])

    # Search top 2 relevant chunks
    _, ids = index.search(q_vec, 2)
    context = " ".join([chunks[i] for i in ids[0]])

    # Build the prompt for T5
    prompt = f"""
You are PadCare GPT — a smart, friendly assistant.
Answer clearly and naturally using ONLY the information below.
Avoid repeating sentences. Keep it simple, human, and easy to read.

--- INFORMATION ---
{context}
--- END INFORMATION ---

Question: {question}
"""

    # Tokenize the prompt (convert text into tokens the model understands)
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate answer
    # do_sample=True and top_p/top_k make the answer more natural and less robotic
    outputs = model.generate(
        **inputs,
        max_new_tokens=250,
        temperature=0.7,
        do_sample=True,
        top_p=0.9,
        top_k=50,
        no_repeat_ngram_size=2
    )

    # Convert tokens back to text
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -------------------------------
# Streamlit interface
# -------------------------------
question = st.text_input("Type your question here:")

if st.button("Ask"):
    if question.strip() != "":
        with st.spinner("Thinking... "):
            answer = padcare_chat(question)
        st.markdown("**Answer:**")
        st.write(answer)
    else:
        st.warning("Please type a question first.")



