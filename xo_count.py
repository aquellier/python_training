import unittest


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertTrue(xo('xxoo'))
        self.assertFalse(xo('xxooo'))
        self.assertTrue(xo(''))
        self.assertTrue(xo('xXOO'))
        self.assertFalse(xo('x'))


if __name__ == '__main__':
    unittest.main()
