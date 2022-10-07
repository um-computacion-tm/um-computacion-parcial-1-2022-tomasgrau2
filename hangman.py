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
        for object1 in self.word:
            if letter.lower() == object1:
                self.correct_letters.append(object1)

