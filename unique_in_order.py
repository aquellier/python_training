import unittest


def unique_in_order(iterable):
    length = len(iterable)
    if length < 2:
        return list(iterable)
    unique_list = [iterable[0]]
    for i in range(1, length):
        if iterable[i-1] != iterable[i]:
            unique_list.append(iterable[i])
    return unique_list

# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result


class Test(unittest.TestCase):

    def test_square_sum(self):
        self.assertEqual(unique_in_order([]), [])
        self.assertEqual(unique_in_order(['A']), ['A'])
        self.assertEqual(unique_in_order(['A', 'A']), ['A'])
        self.assertEqual(unique_in_order(['A', 'A', 'B', 'B', 'C', 'B', 'B']), ['A', 'B', 'C', 'B'])
        self.assertEqual(unique_in_order(['A', 'A', 'B', 'B', 'b', 'C', 'B', 'B']), ['A', 'B', 'b', 'C', 'B'])


if __name__ == '__main__':
    unittest.main()
