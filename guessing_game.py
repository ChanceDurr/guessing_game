from statistics import median
from math import ceil
import kivy
kivy.require('1.11.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Layout(GridLayout):

    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)

        self.cols = 3
        self.guesses = 9
        self.hasWon = False
        self.pressedStart = False
        self.ids.start.text = 'Start'
        self.ids.gameText.text = 'Press Start when you have chosen your number and are ready!'
        self.ids.instructions.text = 'Choose any number between 1 and 300 and I will guess it in 9 tries or less!'
        self.guessList = list(range(0, 301))
        self.guessListNew = []
        self.ids.guessText.text = f'Guess left: {self.guesses}'
        self.currentGuess = 150

    def restart(self):
        self.guesses = 9
        self.hasWon = False
        self.pressedStart = False
        self.ids.start.text = 'Start'
        self.ids.gameText.text = 'Press Start when you have chosen your number and are ready!'
        self.ids.instructions.text = 'Choose any number between 1 and 300 and I will guess it in 9 tries or less!'
        self.guessList = list(range(0, 300))
        self.guessListNew = []
        self.ids.guessText.text = f'Guess left: {self.guesses}'
        self.currentGuess = 150

    def guess(self):
        self.currentGuess = ceil(median(self.guessList))
        return self.currentGuess
     
    def lower(self):
        if self.pressedStart == True and self.hasWon == False:
            self.guesses -= 1
            self.ids.guessText.text = f'Guess left: {self.guesses}'
            self.guessListNew = [i for i in self.guessList if i <= self.currentGuess]
            self.guessList = self.guessListNew
            self.guessListNew = []
            self.ids.gameText.text = f'Is your number {self.guess()}?'
        else:
            pass

    def higher(self):
        if self.pressedStart == True and self.hasWon == False:
            self.guesses -= 1
            self.ids.guessText.text = f'Guess left: {self.guesses}'
            self.guessListNew = [i for i in self.guessList if i >= self.currentGuess]
            self.guessList = self.guessListNew
            self.guessListNew = []
            self.ids.gameText.text = f'Is your number {self.guess()}?'
        else:
            pass
    
    def pressStart(self):
        if self.hasWon == False and self.pressedStart == False:
            self.guesses -= 1
            self.ids.guessText.text = f'Guess left: {self.guesses}'
            self.ids.start.text = 'Correct'
            self.pressedStart = True
            self.ids.gameText.text = f'Is your number {self.currentGuess}?'
        elif self.hasWon == False and self.pressedStart == True:
            self.ids.gameText.text = f'I have won with {self.guesses} guesses left!'
            self.ids.start.text = 'Play Again'
            self.hasWon = True
        else:
            self.restart()


class GuessingGame(App):

    def build(self):
        return Layout()


if __name__ == '__main__':
    GuessingGame().run()