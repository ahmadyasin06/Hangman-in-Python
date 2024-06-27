import random

def hangman():
    installed_words = ["programming", "computer", "coding", "system", "technology", "codefun",
                       "developer", "hangman", "algorithm", "information", "informationtechnology",
                       "python", "pyhtonprogramer", "programmer"]
    
    secret_word = random.choice(installed_words)
    guessed_letters = set()
    print("Welcome to Hangman Game.\n \t Formed by Ahmad Yasin")
    
    attempts = 6
    
    
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word: {display_word}")
        
        if "_" not in display_word:
            print("Congrats, you guessed right!")
            break
        
        guess = input("Guess a letter b/w a-z: ").lower()
        
        if guess in guessed_letters:
            print("You alredy guessed that letter. Try again")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts -= 1
            print(f":( Incorrect! You have {attempts} are left.")
        else:
            print(":) Correct!")
            
        '''if set(secret_word) == guessed_letters:
            print("Congrats! You guessed the word.")
            break'''
        
    if attempts == 0:
        print(f"Sorry you are out of range. The word was {secret_word}")
    
    while True :
        another_game = input("Do you want to play again? (yes/no)").lower()
        if another_game == "no":
           print("Exiting the Hangman Game.\n \t Bye.")
           break
        
        elif another_game == "yes":
            hangman()


hangman()

















'''import random

def hangman():
    installed_words = ["programming", "computer", "coding", "system", "technology", "codefun", "developer", "hangman", "algorithm"]
    secret_word = random.choice(installed_words)
    guessed_letters = set()
    print("Welcome to Hangman Game.\n \t Formed by Ahmad Yasin")
    
    attempts = 6
    
    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word: {display_word}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts -= 1
            print(f":( Incorrect! You have {attempts} attempts left.")
        else:
            print(":) Correct!")
            
        if set(secret_word) == guessed_letters:
            print("Congratulations! You guessed the word.")
            break
            
    if attempts == 0:
        print(f"Sorry, you ran out of attempts. The word was {secret_word}.")

    while True:
        another_game = input("Do you want to play again? (yes/no)").lower()
        if another_game == "no":
            print("Exiting the Hangman Game. Bye.")
            break
        elif another_game == "yes":
            hangman()

hangman()'''
        
