import unittest


def abbrev_name(name):
    return '.'.join(n[0].upper() for n in name.split())


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertEqual(abbrev_name('Antoine Quellier'), 'A.Q')
        self.assertEqual(abbrev_name('A Quellier'), 'A.Q')
        self.assertEqual(abbrev_name('Antoine Q'), 'A.Q')


if __name__ == '__main__':
    unittest.main()
