def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"

        print(display)

        return all(char in guesses for char in secret_word)

    return hangman_closure

#Game

if __name__ == "__main__":
    secret_word = input("Enter the secret word: ")
    game = make_hangman(secret_word)

    solved = False

    while not solved:
        guess = input("Enter a letter: ")
        solved = game(guess)

    print("You got it!")