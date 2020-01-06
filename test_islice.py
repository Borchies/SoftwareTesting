import itertools as it
import unittest


def iterator_to_string(iterator: it):
    """
    Helper function to get a string from the iterator.
    All the elements are appended one after the other, so the string is not unique.

    Examples:
        <aa, ab, ac> => 'aaabac'
        <a, aab, ac> => 'aaabac'
    """
    if iterator is None:
        return None
    result = ''
    for element in iterator:
        result = result + element
    return result


class TestIslice(unittest.TestCase):
    """Test class to test the `itertools.compress` function."""

    def test_example_documentation(self):
        """Example test cases from the documentation."""
        string = 'ABCDEFG'
        self.assertEqual(iterator_to_string(it.islice(string, 2)), 'AB')
        self.assertEqual(iterator_to_string(it.islice(string, 2, 4)), 'CD')
        self.assertEqual(iterator_to_string(it.islice(string, 2, None)), 'CDEFG')
        self.assertEqual(iterator_to_string(it.islice(string, 0, None, 2)), 'ACEG')

    def test_ints_out_bounds(self):
        """Using integer parameters bigger than expected."""
        string = 'ABCDEFG'
        bigger_bounds = len(string) + 1
        self.assertEqual(iterator_to_string(it.islice(string, bigger_bounds)), string)
        self.assertEqual(iterator_to_string(it.islice(string, bigger_bounds, bigger_bounds)), '')
        self.assertEqual(iterator_to_string(it.islice(string, bigger_bounds, bigger_bounds + 5)), '')
        self.assertEqual(iterator_to_string(it.islice(string, bigger_bounds, None)), '')
        self.assertEqual(iterator_to_string(it.islice(string, bigger_bounds, None, 50)), '')

    def test_int_smaller_bounds(self):
        """Using integer parameters smaller than expected, but still positive."""
        string = 'ABCDEFG'
        small_bounds = 0 if len(string) == 0 else int(len(string) / 2)  # Must be int in [0, len(string)-1]
        self.assertEqual(iterator_to_string(it.islice(string, small_bounds)), 'ABC')
        self.assertEqual(iterator_to_string(it.islice(string, 0, 0 if small_bounds == 0 else small_bounds - 1)), 'AB')
        self.assertEqual(iterator_to_string(it.islice(string, small_bounds, small_bounds)), '')
        self.assertEqual(iterator_to_string(it.islice(string, small_bounds, len(string) - 1, small_bounds)), 'D')

    def test_ints_negative(self):
        """
        Using negative integer parameters smaller than expected.
        Raises ValueError because the expected domain of the paramters is [0, maxsize].
        """
        string = 'ABCDEFG'
        smaller_bounds = -1 * (len(string) + 1)
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds, None))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds, -5))

    def test_floats_out_bounds(self):
        """Using floats as parameters, bigger than expected. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        bigger_bounds = float(len(string) + 0.5)
        self.assertRaises(ValueError, lambda: it.islice(string, bigger_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, bigger_bounds, bigger_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, bigger_bounds, bigger_bounds + 5))

    def test_floats_smaller_bounds(self):
        """
        Using floats as parameters, smaller than expected, but still positive.
        Raises ValueError because integers are expected.
        """
        string = 'ABCDEFG'
        smaller_bounds = float(0) if len(string) == 0 else float(len(string) + 0.5)
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds, smaller_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds, 0.7))

    def test_floats_negative(self):
        """Using negative floats as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        smaller_bounds = float(-1 * (len(string) + 1.5))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: it.islice(string, smaller_bounds, None))

    def test_strings(self):
        """Using Strings as paramters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: it.islice(string, 'A'))
        self.assertRaises(ValueError, lambda: it.islice(string, 'a'))
        self.assertRaises(ValueError, lambda: it.islice(string, '0'))
        self.assertRaises(ValueError, lambda: it.islice(string, 'True'))

    def test_booleans(self):
        """
        Using booleans as parameters.
        Although integers are expected, booleans are also accepted. 
        However, only works for the first element in the string.
        """
        string = 'ABCDEFG'
        self.assertEqual(iterator_to_string(it.islice(string, False)), '')
        self.assertEqual(iterator_to_string(it.islice(string, True)), string[0])

    def test_int_list_iterable(self):
        """Using lists of integers as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: it.islice(string, [0, 1]))
        self.assertRaises(ValueError, lambda: it.islice(string, [-1, 7]))

    def test_float_list_iterable(self):
        """Using lists of floats as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: it.islice(string, [-1.75, 1.5]))
        self.assertRaises(ValueError, lambda: it.islice(string, [7.46, 2.93]))

    def test_tuples(self):
        """Using tuples as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: it.islice(string, (None, None)))
        self.assertRaises(ValueError, lambda: it.islice(string, (False, True)))
        self.assertRaises(ValueError, lambda: it.islice(string, (1, 0)))
        self.assertRaises(ValueError, lambda: it.islice(string, ('A', '1')))

    def test_tuple_list_iterable(self):
        """Using lists of tuples as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: it.islice(string, [(True, False), (1, 0)]))        

    def test_nones(self):
        """
        Using None as parameters.
        Raises TypeError when the given string is None.
        Otherwise, returns the string itself.
        """
        string = 'ABCDEFG'
        self.assertRaises(TypeError, lambda: iterator_to_string(it.islice(None, None)))
        self.assertEqual(iterator_to_string(it.islice(string, None)), string)
        self.assertEqual(iterator_to_string(it.islice(string, None, None)), string)
