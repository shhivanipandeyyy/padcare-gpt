# create_index.py
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load sentence transformer
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read raw text
with open("padcare_gpt/data/raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split into chunks (300 chars)
chunks = [text[i:i+300] for i in range(0, len(text), 300)]

# Generate embeddings
embeddings = model.encode(chunks)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and chunks
faiss.write_index(index, "padcare_gpt/index/index.faiss")
pickle.dump(chunks, open("padcare_gpt/index/chunks.pkl", "wb"))

print("FAISS index is ready!")
