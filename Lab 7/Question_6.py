# Write a simple lottery drawing program. The lottery drawing should consist of six different numbers between 1 and 48.

import random
lottery = []
for i in range(6):
    lottery.append(random.randint(1, 48))
print(lottery)