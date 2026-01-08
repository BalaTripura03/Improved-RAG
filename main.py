import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# ----------------------------
# STEP 1: Load PDFs
# ----------------------------
PDF_FOLDER = "data/papers"

print("\n📄 Loading PDF files...\n")

documents = []

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        pdf_path = os.path.join(PDF_FOLDER, file)
        print(f"➡ Loading: {file}")
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())

print(f"\n📘 Total pages loaded: {len(documents)}")

if len(documents) == 0:
    raise ValueError("❌ No PDFs loaded. Check PDF folder path.")

# ----------------------------
# STEP 2: Chunking
# ----------------------------
print("\n✂️ Splitting into chunks...\n")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = text_splitter.split_documents(documents)

print(f"✅ Total chunks created: {len(chunks)}")

# ----------------------------
# STEP 3: Embeddings (FAST MODEL)
# ----------------------------
print("\n🔢 Loading embedding model (fast & lightweight)...\n")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    show_progress=True,
    model_kwargs={"device": "cpu"}
)

# ----------------------------
# STEP 4: Build FAISS
# ----------------------------
print("\n🗄️ Building FAISS vector database...\n")

# Process in batches to avoid memory issues and provide progress feedback
batch_size = 100
print(f"Processing {len(chunks)} chunks in batches of {batch_size}...")

vector_db = None
for i in range(0, len(chunks), batch_size):
    batch = chunks[i:i+batch_size]
    batch_num = (i // batch_size) + 1
    total_batches = (len(chunks) + batch_size - 1) // batch_size
    print(f"  Processing batch {batch_num}/{total_batches}...")
    
    if vector_db is None:
        vector_db = FAISS.from_documents(batch, embeddings)
    else:
        vector_db.add_documents(batch)

print("✅ FAISS index built successfully!")

# ----------------------------
# STEP 5: Query
# ----------------------------
query = input("\n Please enter your query: ")
print(f"\n❓ Query: {query}")

results = vector_db.similarity_search(query, k=3)

print("\n⭐ Top matching chunks:\n")

for i, doc in enumerate(results, start=1):
    print(f"--- Result {i} ---")
    print(doc.page_content[:500])
    print("\n")
