import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'development']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_attempts = 0
    max_attempts = 5  

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    
    while incorrect_attempts < max_attempts:
        print("\nWord to guess: " + display_word(word, guessed_letters))
        print(f"Incorrect attempts left: {max_attempts - incorrect_attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            incorrect_attempts += 1
            print(f"Incorrect guess. You have {max_attempts - incorrect_attempts} attempts left.")
        
        print("Guessed letters: " + ', '.join(sorted(guessed_letters)))
    
    if incorrect_attempts == max_attempts:
        print(f"\nSorry, you're out of attempts. The word was: {word}")

if __name__ == "__main__":
    hangman()
