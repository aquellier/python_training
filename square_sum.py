import unittest


def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


class Test(unittest.TestCase):

    def test_square_sum(self):
        """Should return true sum of squared elements of list"""
        self.assertEqual(square_sum([1, 2, 3]), 14)
        self.assertEqual(square_sum([2]), 4)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([0]), 0)


if __name__ == '__main__':
    unittest.main()
