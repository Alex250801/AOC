data = []

with open("file.txt", "r") as file:
    for line in file.readlines():
        element = []
        for i in line.strip().split(" "):
            element.append(i)
        data.append(element)

total_score = 0
for game in data:
    if game[1] == 'X':
        total_score += 1
    elif game[1] == 'Y':
        total_score += 2
    elif game[1] == 'Z':
        total_score += 3

    if game[0] == 'B' and game[1] == 'Z':
        total_score += 6
    if game[0] == 'A' and game[1] == 'Y':
        total_score += 6
    if game[0] == 'C' and game[1] == 'X':
        total_score += 6
    if game[0] == 'A' and game[1] == 'X':
        total_score += 3
    if game[0] == 'B' and game[1] == 'Y':
        total_score += 3
    if game[0] == 'C' and game[1] == 'Z':
        total_score += 3

print(" Biggest Score is " + str(total_score))


