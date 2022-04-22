# Using the card dictionary from earlier in this chapter, create a simple card game that deals two players three cards each. 
# The player with the highest card wins. If there is a tie, then compare the second highest card and, if necessary, the third highest. 
# If all three cards have the same value, then the game is a draw.

def SimpleCardGame():
    card_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    card_list = []
    for i in range(3):
        card_list.append(input("Enter card: "))
    card_list.sort()
    print(card_list)
    if card_dict[card_list[0]] > card_dict[card_list[1]]:
        print("Player 1 wins")
    elif card_dict[card_list[0]] < card_dict[card_list[1]]:
        print("Player 2 wins")
    else:
        if card_dict[card_list[1]] > card_dict[card_list[2]]:
            print("Player 1 wins")
        elif card_dict[card_list[1]] < card_dict[card_list[2]]:
            print("Player 2 wins")
        else:
            print("Draw")

SimpleCardGame()