import unittest


def reverse_string(string):
    return string[::-1]


class Test(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string('world'), 'dlrow')
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('h'), 'h')


if __name__ == '__main__':
    unittest.main()
