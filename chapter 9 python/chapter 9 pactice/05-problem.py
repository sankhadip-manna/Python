words = ["Mankey", "bad", "ganda"]

# Read file content
with open("file.txt", "r") as f:
    content = f.read()

# Replace each word with #
for word in words:
    content = content.replace(word, "#" * len(word))

# Write back updated content
with open("file.txt", "w") as f:
    f.write(content)
