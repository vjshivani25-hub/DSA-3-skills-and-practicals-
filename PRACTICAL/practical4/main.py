with open("doc1.txt", "r") as file:
    doc1 = file.read()

with open("doc2.txt", "r") as file:
    doc2 = file.read()

words1 = set(doc1.split())
words2 = set(doc2.split())

common = words1.intersection(words2)

print(common)
