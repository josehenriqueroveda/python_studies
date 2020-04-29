import unittest
import guess_game


class TestGame(unittest.TestCase):
    def test_input(self):
        result = guess_game.run_guess(5, 5, 1)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guess_game.run_guess(5, 3, 1)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guess_game.run_guess(11, 7, 1)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
