query = input("Enter query type: ")

if query == "pattern":
    print("KMP Algorithm selected")

elif query == "fuzzy":
    print("Fuzzy Matching selected")

elif query == "similarity":
    print("Document Similarity selected")

else:
    print("No suitable algorithm found")

