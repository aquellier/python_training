import unittest


def printer_error(s):
    # your code
    valid_colors = [chr(i) for i in range(97, 110)]
    return f'{len([letter for letter in s if letter not in valid_colors])}/{len(s)}'


class Test(unittest.TestCase):

    def test_printer_error(self):
        s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        self.assertEqual(printer_error(s), "3/56")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        self.assertEqual(printer_error(s), "6/60")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        self.assertEqual(printer_error(s), "11/65")


if __name__ == '__main__':
    unittest.main()