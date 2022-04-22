# Create a 5*5 list of numbers. Then write a program that creates a dictionary whose keys are the numbers and whose values are the how many times the number occurs. Then print the three most common numbers.

def main():
    list = [[0 for x in range(5)] for y in range(5)]
    for i in range(5):
        for j in range(5):
            list[i][j] = i*j
    print(list)
    dict = {}
    for i in range(5):
        for j in range(5):
            if list[i][j] in dict:
                dict[list[i][j]] += 1
            else:
                dict[list[i][j]] = 1
    print(dict)
    for key in sorted(dict.keys()):
        print(key, dict[key])
    
main()