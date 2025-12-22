with open("text.txt", "r", encoding = "utf-8") as file:
    print("Весенние даты")

for line in file:
    line = line.strip()
    if line == "":
        continue
    
    day, month, year = map(int, line.split())
    if month == 3 or month == 4 or month == 5:
        print(day, month, year)
