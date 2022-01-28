import unittest


def string_end(string, ending):
    return string.endswith(ending)
    # length_ending = len(ending)
    # if length_ending > len(string):
    #     return False
    # target = string[-length_ending:]
    # for i in range(length_ending):
    #     if target[i] != ending[i]:
    #         return False
    # return True


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertFalse(string_end(":-)", ":-("))
        self.assertTrue(string_end("abfdsf", ""))
        self.assertTrue(string_end("abfdsf", "dsf"))
        self.assertTrue(string_end("abfdsf", "abfdsf"))


if __name__ == '__main__':
    unittest.main()


# TAKE AWAY
# Use endswith function