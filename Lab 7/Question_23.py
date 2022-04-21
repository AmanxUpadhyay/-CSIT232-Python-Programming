# Randomly generate a 6*6 List of Assorted characters such that there are exactly two of each character.

import random

MemoryGame = []
for i in range(6):
    MemoryGame.append([])
    for j in range(6):
        MemoryGame[i].append(random.choice(['A', 'B', 'C', 'D', 'E', 'F']))

# Print the list
for i in range(6):
    for j in range(6):
        print(MemoryGame[i][j], end = " ")
    print()
    