# blackjack machine simulator
import random


def cash_in():
    while True:
        amount = input("Type amount of money you want to play with: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Given number must be greater than 0.')
        else:
            print("The number is incorrect. Type another number")
    return amount


CASH = 0
MIN_BET = 1
MAX_BET = 200
CARDS = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,  # A is 1 or 11 depends which is better for the player
}


def player_roll():
    pass


def hands():
    player_hand = []
    player_hand_value = []
    computer_hand = []
    computer_hand_value = []

    while len(player_hand) != 2:
        var_p = random.choice(list(CARDS.keys()))
        val_var_p = CARDS[var_p]
        player_hand.append(var_p)
        player_hand_value.append(int(val_var_p))
        if len(player_hand) == 2:
            print(f"Player's cards are: {player_hand} and it's value is equal to: {sum(player_hand_value)}")

    while len(computer_hand) != 2:
        var_c = random.choice(list(CARDS.keys()))
        val_var_c = CARDS[var_c]
        computer_hand.append(var_c)
        computer_hand_value.append(int(val_var_c))
        if len(computer_hand) == 2:
            print(f"Computer's cards are X and  {player_hand[-1]}"
                  f" and it's value is equal to: {sum(computer_hand_value)}")


def bet():
    while True:
        amount = input("How much would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter the appropriate number.")
    return amount


def main():
    balance = cash_in()
    while True:
        bets = bet()


def game_of_player():
    balance_of_player = 0
    balance_of_computer = 0
    x = player_roll()
    if x == 'player':
        starting_player = balance_of_player
        second_player = balance_of_computer
    else:
        starting_player = balance_of_computer
        second_player = balance_of_player
    while True:
        if starting_player > 21:
            return f'The winner is player with {second_player} points'
        elif second_player > 21:
            return f'The winner is player with {starting_player} points'
        else:
            starting_player += random.choice(list(CARDS.values()))
            print("1:", starting_player)
            x = input("Do you want to bet more in this round? yes/no")
            if x == "yes":
                y = input("How much do you want to bet?")

            elif x == "no":
                continue
            else:
                input("Wrong answer. Do you want to bet more in this round? yes/no")
            second_player += random.choice(list(CARDS.values()))
            print("2:", second_player)


hands()

