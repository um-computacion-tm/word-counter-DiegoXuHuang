import unittest

texto = "Hola amigo como estas amigo. Hola amiga".lower().split(" ")

def count_words(word: str, text: list) -> int:
    return {word: text.count(word)}

if __name__ == '__main__':
    unittest.main()
