with open("articles.txt", "r") as file:
    text = file.read()

query = input("Enter a keyword: ")

if query.lower() in text.lower():
    print("Keyword found.")
else:
    print("Keyword not found.")
