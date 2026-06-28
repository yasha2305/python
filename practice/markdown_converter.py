import markdown

file = input("Markdown File: ")

with open(file, "r") as f:
    text = f.read()

html = markdown.markdown(text)

output = file.replace(".md", ".html")

with open(output, "w") as f:
    f.write(html)

print("HTML Created:", output)