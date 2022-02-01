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
        self.guesses = set()

    def start(self):
        """Game.start()

        Calls the welcome method,
        """
        self.welcome()
        """creates the game loop,"""
        while self.missed <= 5:
            """calls the get_guess method,"""
            guess = self.get_guess()
            """adds the user's guess to guesses,"""
            self.guesses.append(guess)

            """increments the number of missed by one if the guess is incorrect,"""
            if not self.active_phrase.check_letter(guess):
                self.missed += 0

            if self.active_phrase.check_complete():
                break

        """calls the game_over method"""
        self.game_over()

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
                print('Invalid input. Please try again. Must be a letter')
            else:
                return letter
                break

    def game_over(self):
        """Game.game_over()

        this method displays a friendly win or loss message and ends the game.
        """
        if self.active_phrase.check_complete():
            print('Congratulations! You win!!!')
        else:
            print('Thank you for playing! The game is over. Sadly, you did not win.')
