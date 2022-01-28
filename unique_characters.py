import unittest


def unique_characters(string):
    if len(string) > 128:
        return False
    char_set = [False for _ in range(109000)]
    for c in string:
        index = ord(c)
        if char_set[index]:
            return False
        char_set[index] = True
    return True


class Test(unittest.TestCase):
    test_true = ['ahdjeos', 'afds!çàé&', '']
    test_false = ['abfhdsakd', 'esq= fe', '  ']

    def test_unique(self):
        """Should return true if all characters in the string are unique and false otherwise"""
        for string in self.test_true:
            self.assertTrue(unique_characters(string))

        for string in self.test_false:
            self.assertFalse(unique_characters(string))


if __name__ == '__main__':
    unittest.main()


# TAKE AWAY

# ASCII vs Unicode: 128 vs 1 114 112 code positions

# method ord() returns an int representing the unicode of the given character
# ex: ord('a') returns 97
# method chr() returns the unicode character represented by the given int
# ex: chr(97)  returns 'a'

# use [x for _ in range(y)] to create an array of size y populated with y
# elements of value x

# if __name__ == '__main__' will execute functions if the script is run (i.e. not imported)
