from src.load_documents import load_papers

docs = load_papers("data/papers")

print("\n========== EXTRACTION SUMMARY ==========")

for doc in docs:
    print("\nFILE:", doc["filename"])
    print("TEXT LENGTH:", len(doc["text"]))
    print("PREVIEW:")
    print(doc["text"][:200])
