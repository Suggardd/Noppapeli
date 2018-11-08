import random

# Global variables
hand1 = [1, 1]
hand2 = [1, 1]
players = []

# Sets players for the game
def set_players():
    i = 0

    while i <= 1:
        players.append(input(print("Set player" + str(i+1) + " name: ")))
        i += 1

# Sets random number 1-6 to hand variables
def set_dice():
    i = 0
    while i <= 1:
        hand1[i] = random.randint(1, 6)
        hand2[i] = random.randint(1, 6)
        i += 1
    hand1.sort(reverse=True)
    print(players[0] + "'s" + " hand:" + "\n" + "[" + str(hand1[0]) + "]" + " " + "[" + str(hand1[1]) + "]" + "\n")
    hand2.sort(reverse=True)
    print(players[1] + "'s" + " hand:" + "\n" + "[" + str(hand2[0]) + "]" + " " + "[" + str(hand2[1]) + "]" + "\n")


# Compares both hands and declares the winner
def check_dice_sum(h1, h2):
    sum1 = 0
    sum2 = 0

    sum1 = h1[0] + h1[1]
    sum2 = h2[0] + h2[1]

    if sum1 == sum2:
        print("It's a draw! Playing again...")
        set_dice()
        check_dice_sum(hand1, hand2)
    elif sum1 > sum2:
        print("The winner is " + players[0] + "!")
    elif sum2 > sum1:
        print("The winner is " + players[1] + "!")


def main():
    set_players()
    set_dice()
    check_dice_sum(hand1,hand2)


main()




