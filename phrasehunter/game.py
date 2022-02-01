import random
import string

class Game:
    def __init__(self, phrase):
        self.missed = 0
        self.phrases = [Phrase('there is a cat'),
                        Phrase('pizza is delicious'),
                        Phrase('eat dirt for breakfast'),
                        Phrase('there are many patterns in life'),
                        Phrase('save the world')]
        self.active_phrase = None
        self.guesses = []

    def start(self):
        """Game.start()

        Calls the welcome method,
        creates the game loop,
        calls the get_guess method,
        adds the user's guess to guesses,
        increments the number of missed by one if the guess is incorrect,
        calls the game_over method
        """

    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrases)

        return self.active_phrase

    def welcome(self):
        print("""Welcome to the Phrase Hunter game
        By Renee Louise Brinkman
        """)

    def get_guess(self):
        while True:
            letter = input('Guess a letter: ')

            if len(letter) > 1 and letter.lower() not in string.ascii_lowercase:
                print('Invalid letter. Please try again.')
            else:
                self.guesses.append(letter)
                break

    def game_over(self):
        """Game.game_over()

        this method displays a friendly win or loss message and ends the game.
        """
