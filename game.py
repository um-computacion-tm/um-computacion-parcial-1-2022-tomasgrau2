from hangman import Hangman


if __name__ == '__main__':
    hangman = Hangman()
    hangman.set_word(input('Palabra: '))
    print(hangman.play())
