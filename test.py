import unittest
from unittest.mock import patch
from parameterized import parameterized

from hangman import Hangman
from invalidassignmentexception import InvalidAssignmentException


class TestHangman(unittest.TestCase):

    @parameterized.expand([('ahorcado', 'Lifes: 5 - Word: _ _ _ _ _ _ _ _ '),
                           ('casa', 'Lifes: 5 - Word: _ _ _ _ '),
                           ('computacion', 'Lifes: 5 - Word: _ _ _ _ _ _ _ _ _ _ _ ')])
    def test_show(self, word, display):
        hangman = Hangman()
        hangman.set_word(word)
        self.assertEqual(hangman.show(), display)

    @parameterized.expand([('programacion', ['p', 'a', 'o'], 'Lifes: 5 - Word: p _ o _ _ a _ a _ _ o _ '),
                           ('avion', ['a', 'v', 'n'],
                            'Lifes: 5 - Word: a v _ _ n '),
                           ('camion', ['c', 'm', 'n'], 'Lifes: 5 - Word: c _ m _ _ n ')])
    def test_assign(self, word, tries, display):
        hangman = Hangman()
        hangman.set_word(word)
        for letter in tries:
            hangman.assign(letter)
        self.assertEqual(hangman.show(), display)

    @parameterized.expand([('programacion', ['p', 'a', 'z']),
                           ('merienda', ['b', 'b']),
                           ('academia', ['a', 'a', 'a', 'a', 'a', 'f', 'f', 'f'])])
    def test_raise_assign(self, word, tries):
        hangman = Hangman()
        hangman.set_word(word)
        with self.assertRaises(InvalidAssignmentException):
            for letter in tries:
                hangman.assign(letter)

    @parameterized.expand([('inalambrica', ['p', 'a', 'z'], 3),
                           ('caprese', ['i', 'i'], 3),
                           ('online', ['o', 'o', 'o', 'o', 'x', 'x', 'x', 'x'], 1)])
    def test_lifes(self, word, tries, lifes):
        hangman = Hangman()
        hangman.set_word(word)
        for letter in tries:
            try:
                hangman.assign(letter)
            except InvalidAssignmentException:
                pass
        self.assertEqual(hangman.lifes, lifes)

    @parameterized.expand([('palabra', ['a', 'b']),
                           ('ahorcado', ['a', 'h', 'c']),
                           ('electroencefalograma', ['e', 'l', 't', 'r', 'g', 'a'])])
    def test_winner_false(self, word, tries):
        hangman = Hangman()
        hangman.set_word(word)
        for letter in tries:
            hangman.assign(letter)
        self.assertFalse(hangman.winner())

    @parameterized.expand([('WoRkSpAcE', ['w', 'o', 'r', 'k', 's', 'p', 'a', 'c', 'e']),
                           ('PYTHON', ['p', 'y', 't', 'h', 'o', 'n']),
                           ('science', ['S', 'C', 'I', 'e', 'N'])])
    def test_winner_true(self, word, tries):
        hangman = Hangman()
        hangman.set_word(word)
        for letter in tries:
            hangman.assign(letter)
        self.assertTrue(hangman.winner())

    @patch('builtins.input', side_effect=['j', 'a', 'e', 'h', 'r'])
    def test_play_win(self, mock_inputs):
        hangman = Hangman()
        hangman.set_word('jarra')
        self.assertEqual(hangman.play(), 'Ganaste')

    @patch('builtins.input', side_effect=['h', 'j', 'a', 'e', 'l', 'w'])
    def test_play_lost(self, mock_inputs):
        hangman = Hangman()
        hangman.set_word('horno')
        self.assertEqual(hangman.play(), 'Perdiste')


if __name__ == '__main__':
    unittest.main()
