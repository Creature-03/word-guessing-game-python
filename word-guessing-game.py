import random

#initializes an array of words
words = ['dog', 'cat', 'fish', 'elephant', 'giraffe', 'alligator', 'panda', 'sloth', 'donkey']

#picks a random word from $words
target_word = random.choice(words)

#promts the user to guess a word
print("guess the word!")

#initializes the correct characters in the users guess
guesses = ""

#sets turn limit
turns = 15

#initializes the count for the incorrect characters in the users guess
incorrect_characters = 0

#checks if turn limit is reached
while turns > 0

    #initializes the count for number of incorrect characters
    incorrect_characters = 0

    #loops through the characters in $target_word
    for char in target_word:

        #compares each character in $target_word to each character in $guesses and prints the correct characters
        if char in guesses:
            print(char, end=" ")
        else:
            #replace incorrect characters in the users guess with underscores and incriment $incorrect_characters
            print("_")
            incorrect_characters += 1
    
    #wins the game if there are no incorrect characters
    if incorrect_characters == 0:
        print('You win!')
        print('The word is: ', target_word)
        break

    #prompts the user for a guess
    guess = input('Guess a character: ')

    #adds each $guess to #guesses
    guesses += guess

    #decreases turn count and informs the user if $guess is not in $target_word
    if guess not in target_word:
        turns -= 1
        print("Wrong, that letter in not in the word.")
        print("You have ", turns, "more guesses.")

        #loses the game if turns reaches 0
        if turns == 0
        print("You are out of guesses, better luck next time.")