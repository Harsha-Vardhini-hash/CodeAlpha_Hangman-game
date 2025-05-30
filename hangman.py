import random

def hangman():
    word_list = ['apple', 'banana', 'grape', 'orange', 'mango']
    
    word = random.choice(word_list)
    
    guessed_letters = []  # Stores all guessed letters
    attempts_left = 6
    word_display = ['_' for _ in word]  # Display of word

    print("🎮 Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    
    while attempts_left > 0 and '_' in word_display:
        print("\nWord:", ' '.join(word_display))
        print("Guessed letters:", ' '.join(guessed_letters))
        print(f"Attempts left: {attempts_left}")
        
        guess = input("Enter a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single valid letter.")
            continue
        if guess in guessed_letters:
            print("✅ You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print("🎉 Good guess!")
            # Reveal the letter in the word
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            print("❌ Wrong guess.")
            attempts_left -= 1
    
    if '_' not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game over. The word was:", word)

hangman()
