import unittest
import string


def is_pangram(s):
    # lowercase = s.lower()
    # for letter in list(string.ascii_lowercase):
    #     if letter not in lowercase:
    #         return False
    # return True
    return set(string.ascii_lowercase) <= set(s.lower())


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertTrue(is_pangram('abcdefghijklmnopqrstuvwxyz'))
        self.assertTrue(is_pangram('abcdefdsfdsffghijkLMNopqfdsfsrstuvwxyz'))
        self.assertFalse(is_pangram('abcdefghijklmnopqrstuvwxy'))


if __name__ == '__main__':
    unittest.main()
