import itertools as it
import unittest


def iterator_to_list(iterator: it) -> list:
    if iterator is None:
        return None
    result = []
    for element in iterator:
        result.append(element)
    return result


class TestStarmap(unittest.TestCase):
    """Test class to test the `itertools.starmap` function."""

    def test_example_documentation(self):
        """Example test cases from the documentation. This includes the expected input."""
        self.assertEqual(iterator_to_list(it.starmap(pow, [(2, 5)])), [32])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(3, 2)])), [9])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(10, 3)])), [1000])
        self.assertEqual(iterator_to_list(it.starmap(pow, [(2, 5), (3, 2), (10, 3)])), [32, 9, 1000])

    def test_more_arguments(self):
        """More arguments are passed than the given function uses."""
        self.assertRaises(TypeError, it.starmap(float, [(0, 0)]))
        self.assertRaises(TypeError, it.starmap(pow, [(0, False)]))
        self.assertRaises(TypeError, it.starmap(pow, [(0, 'a')]))

    def test_less_arguments(self):
        """Less arguments are passed than the given function uses."""
        self.assertRaises(TypeError, it.starmap(pow, [(5)]))
        self.assertRaises(TypeError, it.starmap(pow, [(2)]))
        self.assertRaises(TypeError, it.starmap(pow, [(3)]))
        self.assertRaises(TypeError, it.starmap(pow, [(5), (2), (3)]))

    def test_none_arguments(self):
        """Nones are passed as arguments."""
        self.assertRaises(TypeError, it.starmap(pow, [(None, 3)]))
        self.assertRaises(TypeError, it.starmap(pow, [(1, None)]))
        self.assertRaises(TypeError, it.starmap(pow, [(None, None)]))

    def test_exception_in_inner_function(self):
        """Launching an exception in the inner function."""
        def my_function(arg):
            raise Exception("Always launches exception")
        self.assertRaises(Exception, it.starmap(my_function, [1, 2, 3]))

    def test_functions_as_arguments(self):
        """Functions are passed as arguments to the main function."""
        def return1():
            return 1

        def return2():
            return 2

        def my_function(func1, func2):
            return func1() + func2()

        self.assertEqual(iterator_to_list(it.starmap(my_function, [(return1, return2), (return2, return1)])), [3, 3])
