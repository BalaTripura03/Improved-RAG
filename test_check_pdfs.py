import os

path = "data/papers"

print("PDFs found:")
for file in os.listdir(path):
    if file.endswith(".pdf"):
        print(file)
