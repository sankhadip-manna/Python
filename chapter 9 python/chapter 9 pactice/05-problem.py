words = ["Mankey", "bad", "ganda"]

# Read file content
with open("file1.txt", "r") as f:
    content = f.read()

# Replace each word with #
for word in words:
    content = content.replace(word, "#" * len(word))

# Write back updated content
with open("file1.txt", "w") as f:
    f.write(content)
