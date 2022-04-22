# Using the card dictionary from earlier in the chapter, deal out three cards. Determine the following:
# (a) If the three cards form a flush (all of the same suit)
# (b) If there is a three-of-a-kind (all of the same value)
# (c) If there is a pair, but not three-of-a-kind
# (d) If the three cards form a straight (all in a row, like (2, 3, 4) or (10, Jack, Queen))

def SimpleCardGame():
    card_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    card_list = []
    for i in range(3):
        card_list.append(input("Enter card: "))
    card_list.sort()
    print(card_list)
    flush = False
    three_of_a_kind = False
    pair = False
    straight = False
    if (card_list[0][1] == card_list[1][1] == card_list[2][1]):
        flush = True
    if (card_dict[card_list[0][0]] == card_dict[card_list[1][0]] == card_dict[card_list[2][0]]):
        three_of_a_kind = True
    if (card_dict[card_list[0][0]] == card_dict[card_list[1][0]] and card_dict[card_list[1][0]] != card_dict[card_list[2][0]]):
        pair = True
    if (card_dict[card_list[0][0]] + 1 == card_dict[card_list[1][0]] and card_dict[card_list[1][0]] + 1 == card_dict[card_list[2][0]]):
        straight = True
    if (flush and three_of_a_kind):
        print("Player 1 wins")
    elif (flush and pair):
        print("Player 2 wins")
    elif (flush and straight):
        print("Player 1 wins")
    elif (three_of_a_kind and pair):
        print("Player 2 wins")
    elif (three_of_a_kind and straight):
        print("Player 1 wins")
    elif (pair and straight):
        print("Player 2 wins")
    else:
        print("Draw")

SimpleCardGame()