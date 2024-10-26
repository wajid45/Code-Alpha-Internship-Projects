import random
import string

def hangman():

    words = ["random","prince","castle","pakistan","cricket","hockey","football"]
    word = random.choice(words)

    used_letters = set()
    tries = len(word)                #Tries will be equal to the length of word
    print("\n Total number of tries: ",tries)

    while tries > 0:
        print("\nAlready used Letters:", " ".join(used_letters))

        guess = input("Guess a letter: ").lower()

        if guess in used_letters:
            print("You had guessed that letter.")
            continue

        if guess not in word:
            tries -= 1
            print("Opss!! Try Again ", tries, " tries left.")

            used_letters.add(guess)

        else:
            print("Well done, nice guess")
            used_letters.add(guess)

        # Check if the word has been guessed
        if all(letter in used_letters for letter in word):
            print("Congratulations, you won!!")
            break

    if tries == 0:
        print("Seems like you lost. The correct word was:", word)

if __name__ == "__main__":
    hangman()
