import itertools as it
import unittest


def compress_str(data, selectors) -> str:
    def iterator_to_str(iterator: it) -> str:
        if iterator is None:
            return ''
        result = ''
        for element in iterator:
            result = result + element
        return result
    return iterator_to_str(it.compress(data, selectors))


class TestCompress(unittest.TestCase):

    def test_example_documentation(self):
        self.assertEqual(compress_str('ABCDEF', [1, 0, 1, 0, 1, 1]), 'ACEF')

    def test_expected_input(self):
        """Expected input == str and binary list, both of same length."""
        self.assertEqual(compress_str('ABC', [0, 0, 0]), '')
        self.assertEqual(compress_str('ABC', [1, 1, 1]), 'ABC')
        self.assertEqual(compress_str('ABC', [1, 0, 1]), 'AC')
        self.assertEqual(compress_str('ABC', [0, 1, 0]), 'B')

    def test_longer_list(self):
        """The length of the list is longer than the length of the string."""
        self.assertEqual(compress_str('ABC', [1, 0, 0, 1, 1, 0, 1]), 'A')
        self.assertEqual(compress_str('ABC', [0 for i in range(10)]), '')
        self.assertEqual(compress_str('ABC', [1 for i in range(10)]), 'ABC')

    def test_none_list(self):
        """The given list is None or a list containing Nones."""
        self.assertRaises(TypeError, lambda: compress_str('ABC', None))
        self.assertRaises(TypeError, lambda: compress_str('', None))
        self.assertEqual(compress_str('ABC', [None, None, None]), '')

    def test_boolean_list_shorter(self):
        """The given list is shorter than the length of the string."""
        self.assertEqual(compress_str('ABCDEF', [0, 0]), '')
        self.assertEqual(compress_str('ABCDEF', [0, 1]), 'B')
        self.assertEqual(compress_str('ABCDEF', [1, 1]), 'AB')

    def test_boolean_list_equal_length(self):
        """A boolean list instead of binary integer list of the same length as the string."""
        self.assertEqual(compress_str('ABC', [False, False, False]), '')
        self.assertEqual(compress_str('ABC', [False, True, False]), 'B')
        self.assertEqual(compress_str('ABC', [True, True, True]), 'ABC')

    def test_boolean_list_longer(self):
        """A boolean list instead of bynary integer list, longer than the length of the string."""
        self.assertEqual(compress_str('ABC', [False, False, False, False]), '')
        self.assertEqual(compress_str('ABC', [False, True, False, True]), 'B')
        self.assertEqual(compress_str('ABC', [True, True, True, True]), 'ABC')

    def test_list_other_integers(self):
        """
        An integer list of same length as the string.

        Returns all but int(0).
        """
        self.assertEqual(compress_str('ABC', [0, 1, 2]), 'BC')
        self.assertEqual(compress_str('ABC', [-2, -1, 0]), 'AB')
        self.assertEqual(compress_str('ABC', [-1000, 0, 1000]), 'AC')

    def test_list_strs(self):
        """
        A string list of same length as the string.

        Returns all but int(0). Strings are used in this test, so only '' matches with False.
        """
        self.assertEqual(compress_str('ABC', ['a', 'b', 'c']), 'ABC')
        self.assertEqual(compress_str('ABC', ['0', '1', '2']), 'ABC')
        self.assertEqual(compress_str('ABC', ['.', '', '-']), 'AC')

    def test_float(self):
        """
        A float list of same length as the string.
        """
        self.assertEqual(compress_str('ABC', [-1.0, 0, 1.0]), 'AC')
        self.assertEqual(compress_str('ABC', [-10.5, 29.3, 0]), 'AB')
        self.assertEqual(compress_str('ABC', [-0.0, +0.0, 1]), 'C')

    def test_list_multiple_types(self):
        """
        A list containing items of multiple types.

        Multiple types is viable. Only 0, False and '' don't match.
        """
        self.assertEqual(compress_str('ABC', [False, 1.0, 'a']), 'BC')
        self.assertEqual(compress_str('ABC', [True, -9, '']), 'AB')
        self.assertEqual(compress_str('ABC', [None, 0, True]), 'C')
