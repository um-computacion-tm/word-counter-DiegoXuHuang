import unittest
from count_words import count_words


class TestCountLetters(unittest.TestCase):

    
    def test_simple(self):
        word = "hola"
        result = count_words(word,texto)
        self.assertEqual(result, {word:2})

    def test_simple(self):
        word = "amigo"
        result = count_words(word,texto)
        self.assertEqual(result, {word:1})
    
    def test_simple(self):
        word = "como"
        result = count_words(word,texto)
        self.assertEqual(result, {word:1})

    def test_simple(self):
        word = "amiga"
        result = count_words(word,texto)
        self.assertEqual(result, {word:1})

if __name__ == '__main__':
    unittest.main()