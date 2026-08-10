with open("sample.txt", "r") as file:
    text = file.read()

pattern = input("Enter the pattern: ")

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        print("Pattern found at", i)
