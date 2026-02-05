# PadCare GPT – Human-friendly Q&A, Summaries, and Posts
# This version uses a causal LM (GPT2) for natural, readable answers

from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer
import faiss
import pickle

# ----------------------------
# Load models
# ----------------------------
# Sentence transformer for embedding questions
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Causal LM for generating natural language answers
# GPT2 is used here because T5 is text2text and caused prompt-only output
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")

# ----------------------------
# Load FAISS index and text chunks
# ----------------------------
index = faiss.read_index("padcare_gpt/index/index.faiss")
chunks = pickle.load(open("padcare_gpt/index/chunks.pkl", "rb"))


def padcare_chat(question):
    """
    PadCare GPT: Answer questions about PadCare Labs in a friendly, natural, and human way.
    - Simple questions: 1-3 paragraphs
    - Summaries: bullet points
    - Posts/pitches: lively and professional
    - Always stay true to the provided information, do not hallucinate.
    """

    # Convert question to embedding vector
    q_vec = embedder.encode([question])

    # Search top 2 relevant chunks
    _, ids = index.search(q_vec, 2)
    context = " ".join([chunks[i] for i in ids[0]])

    # Build a natural, human-friendly prompt
    prompt = f"""
You are PadCare GPT — a smart, friendly assistant who explains things clearly and naturally.
Use ONLY the information below. Avoid repeating sentences. Make it simple, human, and easy to read.
- For simple questions: 1-3 paragraphs
- For summaries: bullet points
- For posts or pitches: lively, professional, friendly

--- INFORMATION START ---
{context}
--- INFORMATION END ---

Question: {question}
"""

    #Tokenize the prompt
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate the answer
    outputs = model.generate(
        **inputs,
        max_new_tokens=400,    # Enough length for paragraphs
        temperature=0.7,       # Makes output more natural
        do_sample=True,
        top_p=0.9,
        top_k=50,
        no_repeat_ngram_size=2
    )

    # Decode tokens into human-readable text
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer
