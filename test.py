import unittest

from bingo import Bingo

class TestCases(unittest.TestCase):
    def test_bingo(self):
        b = Bingo("1")
        self.assertEqual(b.bingoRound(), "Player 1 is the winner!")

    def test_bingo_letters(self):
        b = Bingo("a")
        self.assertEqual(b.bingoRound(), "That's not a valid entry. Please, type a number.")
        b = Bingo("-1234")
        self.assertEqual(b.bingoRound(), "That's not a valid entry. Please, type a number.")

    def test_bingo_range(self):
        b = Bingo("0")
        self.assertEqual(b.bingoRound(), "That number is not within the valid range.")
        b = Bingo("15040503503")
        self.assertEqual(b.bingoRound(), "That number is not within the valid range.")

if __name__ == "__main__":
    unittest.main(verbosity=2)