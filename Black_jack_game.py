# alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# word=input("Please enter the input text:")
#
# shift_amount=int(input("Please enter the shift amount:"))
# def cipher_text(word):
#     for letter in word:
#         secret_word=""
#         shifted_position=alphabet.index(letter)-shift_amount
#         shifted_position %= len(alphabet)
#         secret_word+=alphabet[shifted_position]
#         print(f"{secret_word}")
# cipher_text(word)

# import random
# is_game_on=True
# cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
# dealer=[]
# player=[]
# is_continue=True
# def black_jack():
#     choice=input("Do you want to play BlackJack? Y or N").strip().lower()
#     if choice=='n':
#         is_game_on=False
#     elif choice=='y':
#         player.append(random.choice(cards))
#         dealer.append(random.choice(cards))
#         print(f"Player's first card: {player}")
#         print(f"Dealer's first card: {dealer}")
#         continue_game=input("Do you want to draw one more card (y or n)?").strip().lower()
#         if continue_game=="y":
#             black_jack()
#         else:
#             is_continue=False
#
#     else:
#         print("Please Enter a valid input")


import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer = []
player = []

def black_jack():
    global is_game_on
    global is_continue

    is_game_on = True
    is_continue = True

    choice = input("Do you want to play BlackJack? Y or N: ").strip().lower()

    if choice == 'n':
        is_game_on = False
        return
    elif choice == 'y':
        player.append(random.choice(cards))
        dealer.append(random.choice(cards))
        print(f"Player's first card: {player}")
        print(f"Dealer's first card: {dealer[0]}")  # show only one dealer card

        while is_continue:
            continue_game = input("Do you want to draw one more card (y or n)? ").strip().lower()
            if continue_game == "y":
                player.append(random.choice(cards))
                print(f"Player's cards: {player}")
                print(f"Current total: {sum(player)}")
                dealer.append(random.choice(cards))

                if sum(player) > 21:
                    print("You went over 21. You lose!")
                    break
            else:
                is_continue = False
                print("Game stopped.")
                print(f"Your final hand: {player} (Total: {sum(player)})")
                print(f"Dealer's hand: {dealer} (Total: {sum(dealer)})")
                if sum(dealer)>sum(player) and sum(dealer)<=21:
                    print("You have lost")
                elif sum(player)>sum(dealer) and sum(player)<=21:
                    print("You won")


    else:
        print("Please enter a valid input. (y or n)")
        black_jack()

black_jack()

