import unittest
from collections import Counter


def count_sheep(array_of_sheep):
    return Counter(array_of_sheep)[True]
    # return array_of_sheep.count(True)


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertEqual(count_sheep([True, True, False]), 2)
        self.assertEqual(count_sheep([True, True, None]), 2)
        self.assertEqual(count_sheep([]), 0)


if __name__ == '__main__':
    unittest.main()
