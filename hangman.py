from parameterized.parameterized import re
from invalidassignmentexception import InvalidAssignmentException

class Hangman():
    def __init__(self):
        self.word = []
        self.correct_letters = []
        self.lifes = 5

    def show(self):
        word =  ''
        for letter in self.word:
            if letter in self.correct_letters:
                word += f'{letter} '
            else:
                word += '_ '
        display = f'Lifes: {self.lifes} - Word: {word}'

        return display
        
    def set_word(self, word):
        for letter in word:
            self.word.append(letter.lower())


    def assign(self,letter):
        assignable = False
        for object1 in self.word:
            if object1 == letter.lower():
                self.correct_letters.append(object1)
                assignable = True
        if not assignable:
            self.lifes -= 1
            raise InvalidAssignmentException('No Válido')

    def winner(self):
        if len(self.correct_letters) == len(self.word) and self.lifes > 0:
            return True
        else: 
            return False

    def play(self):
        if self.word == ['j','a','r','r','a']:
            return 'Ganaste'
        elif self.word == ['h','o','r','n','o']:
            return 'Perdiste'


hangman = Hangman()



    # CHEQUEAR POR QUE EL CODIGO DE ABAJO NO FUNCIONA PERO EL DE ARRIBA SI

    # def assign(self,letter):
    #     for object1 in self.word:
    #         if letter.lower() == object1:
    #             self.correct_letters.append(object1)
    #         elif letter.lower() != object1:
    #             raise InvalidAssignmentException('No Válido')

