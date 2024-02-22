import random

def choose_word():
    words = ["apple", "banana", "orange", "grape"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    attempts = 7
    
    print()
    print(" Welcome to Hangman! ")
    print("Try to guess the word.")

    while True:
        guessed_letters = []  
        while attempts > 0:
            print("\n" + display_word(word, guessed_letters))
            guess = input("Enter a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                print("Correct!")
                guessed_letters.append(guess)
                if display_word(word, guessed_letters) == word:
                    print("Congratulations! You guessed the word:", word)
                    break
            else:
                print("Incorrect!")
                attempts -= 1
                print("Attempts left:", attempts)
                if attempts == 0:
                    print("Sorry, you're out of attempts. The word was:", word)
                    break
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    hangman()