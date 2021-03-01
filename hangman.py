import random
#
# def hangman(word):
#     wrong = 0
#     stages = ["",
#               "                ",
#               "_________       ",
#               "|       |       ",
#               "|       |       ",
#               "|       O       ",
#               "|     /| |\     ",
#               "|      / \      ",
#               "|               ",
#               ]
#     rletters = list(word)
#     board = ["_"] * len(word)
#     win = False
#     print("Welcome to Hangman!")
#
#     while wrong < len(stages) -1:
#         print("\n")
#         msg = "1文字を予想してね: "
#         char = input(msg)
#         if char in rletters:
#             cind = rletters.index(char)
#             board[cind] = char
#             rletters[cind] = '$'
#         else:
#             wrong += 1
#         print(" ".join(board))
#         e = wrong + 1
#         print("\n".join(stages[0:e]))
#         if "_" not in board:
#             print("You win!")
#             print(" ".join(board))
#             win = True
#             break
#     if not win:
#         print("\n".join(stages[0:wrong+1]))
#         print("You lose! The Answer is {}.".format(word))
#
# word_list = ["great", "dangeraus", "america", "python", "question", "programmer", "japan",
#              "world", "iost", "increment", "choice", "river", "mountain", "sea", "phone",
#              "apple", "google", "tesla", "bitcoin", "tennis", "sllep", "airpods", "book"]
#
#
# word = random.choice(word_list)
# hangman(word)


def hangman():
    word_list = ["great", "dangeraus", "america", "python", "question", "programmer", "japan",
                 "world", "iost", "increment", "choice", "river", "mountain", "sea", "phone",
                 "apple", "google", "tesla", "bitcoin", "tennis", "sllep", "airpods", "book"]
    random_number = random.randint(0, 23)
    word = word_list[random_number]
    wrong_guesses = 0
    stages = ["",
              "                ",
              "_________       ",
              "|       |       ",
              "|       |       ",
              "|       O       ",
              "|     /| |\     ",
              "|      / \      ",
              "|               ",
              ]
    remaining_letters = list(word)
    letter_board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")

    while wrong_guesses < len(stages) -1:
        print("\n")
        guess = input("1文字を予想してね: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print(" ".join(letter_board))
        e = wrong_guesses + 1
        print("\n".join(stages[0:e]))
        if "_" not in letter_board:
            print("You win!")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong_guesses+1]))
        print("You lose! The Answer is {}.".format(word))



# word = random.choice(word_list)
hangman()