import random

def get_word():
    words = ["python", "zainu", "dynamic", "programming", "challenge", "faiqadon"]
    return random.choice(words).upper()

def print_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     /
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
          ---
        """,
        """
           --------
           |      |
           |
           |
           |
           |
          ---
        """
    ]
    print(stages[tries])

def hangman():
    word = get_word()
    word_completion = ["_"] * len(word)
    guessed = set()
    tries = 6
    
    print("Let's play Hangman!")
    print_hangman(tries)
    print(" ".join(word_completion))
    
    while tries > 0 and "_" in word_completion:
        guess = input("Guess a letter:").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        
        guessed.add(guess)
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_completion[i] = guess
        else:
            tries -= 1
            print("Incorrect guess!")
        
        print_hangman(tries)
        print(" ".join(word_completion))
    
    if "_" not in word_completion:
        print("Congratulations! You guessed the word.")
    else:
        print(f"Game over! The word was {word}.")

if __name__ == "__main__":
    hangman()
