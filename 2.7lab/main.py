with open ("text.txt", "r", encoding = "utf-8") as file:
    paragraph = 0
    in_paragraph = False

for line in file:
    if line.strip():
        if not in_paragraph:
            paragraph +=1
            in_paragraph = True
        else:
            in_paragraph = False
            
print(paragraph)
