import itertools as it
from itertools import *
import unittest
import operator
import numpy as np
from decimal import Decimal
from fractions import Fraction
import code_anwar

def iterator_to_list(iterator: it) -> list:
    if iterator is None:
        return None
    result = []
    for element in iterator:
        result.append(element)
    return result


def lzip(*args):
    return list(zip(*args))


class Test_itertools(unittest.TestCase):
    '''
    it.count:
    Make an iterator that returns evenly spaced values starting with number start. 
    Often used as an argument to map() to generate consecutive data points. 
    Also, used with zip() to add sequence numbers.
    First test     tests for default method call without input
    Second test    tests for method call with positive offset
    Third test    tests for method call with negative offset
    Fourth test     tests for method call with offset and positive it.counter
    Fifth test    tests for method call with offset and negative it.counter
    Sixth test    tests for method call with offset and 0-it.counter
    Seventh test    tests for method call with non-integer offset and non-integer it.counter
    Eighth test    tests for too many arguments
    Nineth test    tests for non-numerical arguments
    Tenth test    tests for mixed-type arguments
    '''
    def test_count(self):
        # Correct uses
        self.assertEqual(lzip('abc',  it.count()), [('a', 0), ('b', 1), ('c', 2)])
        self.assertEqual(lzip('abc',  it.count(4)), [('a', 4), ('b', 5), ('c', 6)])
        self.assertEqual(lzip('abc',  it.count(-10)), [('a', -10), ('b', -9), ('c', -8)])
        self.assertEqual(lzip('abc',  it.count(4,2)), [('a', 4), ('b', 6), ('c', 8)])
        self.assertEqual(lzip('abc',  it.count(4,-1)), [('a', 4), ('b', 3), ('c', 2)])
        self.assertEqual(lzip('abc',  it.count(4,0)), [('a', 4), ('b', 4), ('c', 4)])
        self.assertEqual(lzip('abc',  it.count(1.5,0.25)), [('a', 1.5), ('b', 1.75), ('c', 2)])
        # Type Errors
        self.assertRaises(TypeError,  it.count, 2,3,4)
        self.assertRaises(TypeError,  it.count, 'a')
        self.assertRaises(TypeError,  it.count, 2, 'c')
        
        
        
    '''
    it.zip_longest:
    Make an iterator that aggregates elements from each of the iterables. 
    If the iterables are of uneven length, missing values are filled-in with fillvalue. 
    Iteration continues until the longest iterable is exhausted. 
    Tests the five cases in test_values with and without a fillvalue.
    Tests for default method call
    Tests for empty list as input
    Tests for TypeError with integer
    Tests for TypeError with None
    '''
    
    def test_zip_longest(self):
        # Define instances to test with
        # Strings
        # Strings and Integer arrays with different length
        # Positive Integers arrays with different length
        # Positive and negative Integer arrays with different length
        # Positive and negative Integer arrays with different length and empty lists
        
        test_values = [['abc'],
            ['abc', range(4)],
            [range(789), range(1987,2100), range(100,150)],
            [range(1000), range(0), range(-100,150), range(120), range(420)],
            [range(1000), [], range(0), range(100,150), range(-120,120), range(420), []]]
        
        for args in test_values:
            # generate test result manually
            target = [tuple([arg[i] if i < len(arg) else None for arg in args])
                      for i in range(max(map(len, args)))]
            
            self.assertEqual(list(it.zip_longest(*args)), target)
            self.assertEqual(list(it.zip_longest(*args, **{})), target)
            
            # replace None with fillvalue manually
            target = [tuple((e is None and 'X' or e) for e in t) for t in target]   
            self.assertEqual(list(it.zip_longest(*args, **dict(fillvalue='X'))), target)
        
        self.assertEqual(list(it.zip_longest()), list(zip()))
        self.assertEqual(list(it.zip_longest([])), list(zip([])))
    
        # Type Errors
        self.assertRaises(TypeError, it.zip_longest, '12345678', 45)
        self.assertRaises(TypeError, it.zip_longest, 3)
        self.assertRaises(TypeError, it.zip_longest, None)

        
    '''
    Make an iterator that returns it.accumulated sums, or it.accumulated results of other binary functions (specified via the optional func argument).
    If func is supplied, it should be a function of two arguments. 
    Elements of the input iterable may be any type that can be accepted as arguments to func. (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)
    Usually, the number of elements output matches the input iterable. 
    However, if the keyword argument initial is provided, the accumulation leads off with the initial value so that the output has one more element than the input iterable.
    First test    tests for strings 
    Tests for different type of numerical values: int, complex, decimal, fraction
    Tests for empty lists, lists with only one entry, negative integers and floats with and without the initial keyword 
    Tests the operator-keyword
    Type Error Tests:
        test for too little arguments
        test for too many arguments
        test for mixed-type arguments
    '''
      
    def test_accumulate(self):    
             
        self.assertEqual(list(it.accumulate('abcd', initial = None)),['a', 'ab', 'abc','abcd'])        
        for typ in int, complex, Decimal, Fraction:                
            self.assertEqual(
                list(it.accumulate(map(typ, range(10)))),
                list(map(typ, [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])))
        
        # initialise test values
        init = 100    
        test_values = [[],[7],np.arange(-10,0),np.arange(0.0, 1.0, 0.1)]
        
        
        for args in test_values:
        
            # Test with default addition operator
            target = []
            target_offset = [init]
            current = 0
            current_offset = init
            for i in args:
                current += i
                current_offset += i
                target.append(current)    
                target_offset.append(current_offset)
                
            self.assertEqual(list(it.accumulate([*args], initial=None)), target)
            self.assertEqual(list(it.accumulate([*args], initial=init)), target_offset)

            
            
            # Test with multiplication operator
            target = []
            target_offset = [init]
            current = 1
            current_offset = init
            for i in args:
                current *= i
                current_offset *= i
                target.append(current)    
                target_offset.append(current_offset)
            self.assertEqual(list(it.accumulate([*args], operator.mul, initial = None)), target)        
            self.assertEqual(list(it.accumulate([*args], operator.mul, initial=init)), target_offset)    
            
            
            # Test with max operator
            target = []
            target_offset = [init]
            current = -10000000
            current_offset = init
            for i in args:
                if i > current: current = i 
                if i > current_offset: current_offset = i
                target.append(current)
                target_offset.append(current_offset)
            self.assertEqual(list(it.accumulate([*args], max, initial = None)), target)    
            self.assertEqual(list(it.accumulate([*args], max, initial=init)), target_offset)    

            # Test with min operator
            current = 10000000
            target = []
            current_offset = init
            target_offset = [init]
            for i in args:
                if i < current: current = i 
                if i < current_offset: current_offset = i
                target.append(current)
                target_offset.append(current_offset)
            self.assertEqual(list(it.accumulate([*args], min, initial = None)), target)        
            self.assertEqual(list(it.accumulate([*args], min, initial=init)), target_offset)    

        # Type Errors    
        self.assertRaises(TypeError, it.accumulate)                             
        self.assertRaises(TypeError, it.accumulate, [1,2,3,], operator.mul, 2) 
        self.assertRaises(TypeError, list, it.accumulate([1, 'a']))        
        

class Itertools_MyTest(unittest.TestCase):

    def setUp(self):
        
        self.posList1 = [7,8,9]
        self.posList2 = [10,11,12]

        self.negList1 = [-1,-2,-3,-4]
        self.negList2= [-10,-11,-12]

        self.floatList1 = [10.15,1.5,8.5]
        self.floatList2 = [-1.0,-2.5,99.99,100.1,5599,777] #mixed decimal list

        self.strList1= ['Hello'] 
        self.strList2 = ['World']

        self.emptyList1= []
        self.emptyList2= []

        self.multiList1=[8.9,-8,(1,4),"Welcome!",5,'',-20]

        self.intValue= 12
        self.strValue1 = "Hi"
        

    def test_for_product(self):

        result = list(it.product(self.posList2))
        self.assertEqual(result,([(10,),(11,),(12,)])) #Testing list of positive values without it.repeat argument           

        result = list(it.product(self.negList1,self.emptyList1))
        self.assertEqual(result,([])) #Testing list of negative values with empty list and without it.repeat argument       

        result = list(it.product(self.floatList1,self.strList1,repeat=1))
        self.assertEqual(result,([(10.15, 'Hello'), (1.5, 'Hello'), (8.5, 'Hello')])) #Testing list of float and string values with repaet argument
       
        result = list(it.product(self.floatList2,self.strList2,self.emptyList1,repeat=1))
        self.assertEqual(result,([])) #Testing multiple iterable list with empty list 
        
        result = list(it.product(self.strValue1,repeat=2))
        self.assertEqual(result,([('H', 'H'), ('H', 'i'), ('i', 'H'), ('i', 'i')])) #Testing string value with it.repeat argument
        
        result = list(it.product())
        self.assertEqual(result,([()])) #Testing without aruguments          

        result = list(it.product(self.multiList1,repeat=1))
        self.assertEqual(result,([(8.9,), (-8,), ((1, 4),), ('Welcome!',), (5,), ('',), (-20,)])) #Testing polymorphic list
       
        result = list(it.product(*self.strList2))
        self.assertEqual(result,([('W',), ('o',), ('r',), ('l',), ('d',)])) #Testing list of positive values without it.repeat argument
        
        range1 = list(it.product(range(5)))
        self.assertEqual(range1,([(0,), (1,), (2,),(3,),(4,)])) #Testing for range of positive value         

        self.assertRaises(TypeError,it.product,self.intValue,repeat=2) #testing TypeError: integer object is not an iterable
        self.assertRaises(TypeError,it.product,self.strValue1,repeat=2.5) #testing TypeError: integer argument expected, got float        
        self.assertRaises(TypeError,it.product,self.strValue1,repeat='12')  # Testing TypeError: 'string' object cannot be interpreted as an integer
        self.assertRaises(OverflowError,it.product,self.strList2,repeat=8**60) #testing OverflowError: Python int too large to convert to C ssize_t


        

    def test_for_chain(self):
       
        it.chainlist = list(it.chain(self.posList1,self.posList2))
        self.assertListEqual(it.chainlist, [7,8,9,10,11,12]) #Testing with list of positive values        

        it.chainlist = list(it.chain(self.negList1,self.negList2))
        self.assertListEqual(it.chainlist, [-1,-2,-3,-4,-10,-11,-12]) #Testing with list of negative values        

        it.chainlist = list(it.chain(self.posList1,self.negList2)) #Testing with list of positive and negative values
        self.assertListEqual(it.chainlist,[7,8,9,-10,-11,-12])          
        
        it.chainlist = list(it.chain(self.posList1,self.posList1)) #Testing for same list/single list
        self.assertListEqual(it.chainlist, [7,8,9,7,8,9])        

        it.chainlist = list(it.chain(self.posList1,self.floatList2)) #Testing with list of positive and decimal values
        self.assertListEqual(it.chainlist,[7,8,9,-1.0,-2.5,99.99,100.1,5599,777])
        
        it.chainlist = list(it.chain(self.strList1,self.strList2)) #Testing for list of string values
        self.assertListEqual(it.chainlist,['Hello', 'World'])
        
        it.chainlist = list(it.chain())
        self.assertListEqual(it.chainlist,[]) #Testing without argument

        it.chainlist = list(it.chain(self.strList1,it.chain(self.negList2,it.chain(self.floatList1)))) #Testing for multiple it.chain()
        self.assertListEqual(it.chainlist,['Hello', -10, -11, -12, 10.15, 1.5, 8.5])
                
        it.chainMixedList = list(it.chain(self.strList1,self.negList1,self.posList2,self.floatList2)) #Testing with list of mixed values
        self.assertListEqual(it.chainMixedList,['Hello',-1,-2,-3,-4,10,11,12,-1.0,-2.5,99.99,100.1,5599,777])        

        emptyList = list(it.chain(self.emptyList1,self.emptyList2)) #Testing for empty list
        self.assertListEqual(emptyList, [])
        
        multiList = list(it.chain(self.multiList1,self.emptyList2))
        self.assertListEqual(multiList, [8.9,-8,(1, 4),'Welcome!',5,'',-20]) #Testing multi value list and empty list        

        stringValue = (list(it.chain(self.strValue1,self.strValue1)))
        self.assertListEqual(stringValue,['H','i','H','i']) #Testing for string value           
      

               
    

    def test_for_repeat(self):

        result = list(it.repeat(self.strValue1,2))       
        self.assertEqual(result,['Hi','Hi']) #Testing with string      

        result = list(it.repeat(self.intValue,5))       
        self.assertEqual(result,[12,12,12,12,12]) #Testing with integer             

        result = list(it.repeat(self.strList1,5))       
        self.assertEqual(result,[['Hello'],['Hello'],['Hello'],['Hello'],['Hello']]) #Testing with string list         

        result = list(it.repeat("",3))
        self.assertEqual(result,['', '', '']) #Testing with empty string        

        result = list(it.repeat(self.emptyList1,3))
        self.assertEqual(result,[[],[],[]]) #Testing with empty List         

        result = list(it.repeat(self.strValue1, 0))
        self.assertEqual(result,[]) #testing a string with 0 cycles         

        result = list(it.repeat(self.multiList1, 2))
        self.assertEqual(result,[[8.9, -8, (1, 4), 'Welcome!', 5, '', -20], [8.9, -8, (1, 4), 'Welcome!', 5, '', -20]]) ##testing a list with different type of values
    
        result = list(it.repeat(self.negList2, 2**2))
        self.assertEqual(result,[[-10, -11, -12], [-10, -11, -12], [-10, -11, -12], [-10, -11, -12]]) #testing with list of negative values 
        

        self.assertRaises(TypeError, it.repeat) # testing TypeError: no argument given
        self.assertRaises(TypeError, it.repeat,self.intValue,self.strValue1,3) #Testing Type Error with extra argument
        self.assertRaises(TypeError, it.repeat,self.intValue,5.7) # testing typeError:- integer argument expected, got float
        self.assertRaises(OverflowError,it.repeat,self.strList2,4**40) #testing OverflowError: Python int too large to convert to C ssize_t




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


class Testit_islice(unittest.TestCase):
    """Test class to test the `itertools.compress` function."""

    def test_example_documentation(self):
        """Example test cases from the documentation."""
        string = 'ABCDEFG'
        self.assertEqual(iterator_to_string(islice(string, 2)), 'AB')
        self.assertEqual(iterator_to_string(islice(string, 2, 4)), 'CD')
        self.assertEqual(iterator_to_string(islice(string, 2, None)), 'CDEFG')
        self.assertEqual(iterator_to_string(islice(string, 0, None, 2)), 'ACEG')

    def test_ints_out_bounds(self):
        """Using integer parameters bigger than expected."""
        string = 'ABCDEFG'
        bigger_bounds = len(string) + 1
        self.assertEqual(iterator_to_string(islice(string, bigger_bounds)), string)
        self.assertEqual(iterator_to_string(islice(string, bigger_bounds, bigger_bounds)), '')
        self.assertEqual(iterator_to_string(islice(string, bigger_bounds, bigger_bounds + 5)), '')
        self.assertEqual(iterator_to_string(islice(string, bigger_bounds, None)), '')
        self.assertEqual(iterator_to_string(islice(string, bigger_bounds, None, 50)), '')

    def test_int_smaller_bounds(self):
        """Using integer parameters smaller than expected, but still positive."""
        string = 'ABCDEFG'
        small_bounds = 0 if len(string) == 0 else int(len(string) / 2)  # Must be int in [0, len(string)-1]
        self.assertEqual(iterator_to_string(islice(string, small_bounds)), 'ABC')
        self.assertEqual(iterator_to_string(islice(string, 0, 0 if small_bounds == 0 else small_bounds - 1)), 'AB')
        self.assertEqual(iterator_to_string(islice(string, small_bounds, small_bounds)), '')
        self.assertEqual(iterator_to_string(islice(string, small_bounds, len(string) - 1, small_bounds)), 'D')

    def test_ints_negative(self):
        """
        Using negative integer parameters smaller than expected.
        Raises ValueError because the expected domain of the paramters is [0, maxsize].
        """
        string = 'ABCDEFG'
        smaller_bounds = -1 * (len(string) + 1)
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds, None))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds, -5))

    def test_floats_out_bounds(self):
        """Using floats as parameters, bigger than expected. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        bigger_bounds = float(len(string) + 0.5)
        self.assertRaises(ValueError, lambda: islice(string, bigger_bounds))
        self.assertRaises(ValueError, lambda: islice(string, bigger_bounds, bigger_bounds))
        self.assertRaises(ValueError, lambda: islice(string, bigger_bounds, bigger_bounds + 5))

    def test_floats_smaller_bounds(self):
        """
        Using floats as parameters, smaller than expected, but still positive.
        Raises ValueError because integers are expected.
        """
        string = 'ABCDEFG'
        smaller_bounds = float(0) if len(string) == 0 else float(len(string) + 0.5)
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds, smaller_bounds))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds, 0.7))

    def test_floats_negative(self):
        """Using negative floats as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        smaller_bounds = float(-1 * (len(string) + 1.5))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds))
        self.assertRaises(ValueError, lambda: islice(string, smaller_bounds, None))

    def test_strings(self):
        """Using Strings as paramters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: islice(string, 'A'))
        self.assertRaises(ValueError, lambda: islice(string, 'a'))
        self.assertRaises(ValueError, lambda: islice(string, '0'))
        self.assertRaises(ValueError, lambda: islice(string, 'True'))

    def test_booleans(self):
        """
        Using booleans as parameters.
        Although integers are expected, booleans are also accepted. 
        However, only works for the first element in the string.
        """
        string = 'ABCDEFG'
        self.assertEqual(iterator_to_string(islice(string, False)), '')
        self.assertEqual(iterator_to_string(islice(string, True)), string[0])

    def test_int_list_iterable(self):
        """Using lists of integers as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: islice(string, [0, 1]))
        self.assertRaises(ValueError, lambda: islice(string, [-1, 7]))

    def test_float_list_iterable(self):
        """Using lists of floats as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: islice(string, [-1.75, 1.5]))
        self.assertRaises(ValueError, lambda: islice(string, [7.46, 2.93]))

    def test_tuples(self):
        """Using tuples as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: islice(string, (None, None)))
        self.assertRaises(ValueError, lambda: islice(string, (False, True)))
        self.assertRaises(ValueError, lambda: islice(string, (1, 0)))
        self.assertRaises(ValueError, lambda: islice(string, ('A', '1')))

    def test_tuple_list_iterable(self):
        """Using lists of tuples as parameters. Raises ValueError because integers are expected."""
        string = 'ABCDEFG'
        self.assertRaises(ValueError, lambda: islice(string, [(True, False), (1, 0)]))        

    def test_nones(self):
        """
        Using None as parameters.
        Raises TypeError when the given string is None.
        Otherwise, returns the string itself.
        """
        string = 'ABCDEFG'
        self.assertRaises(TypeError, lambda: iterator_to_string(islice(None, None)))
        self.assertEqual(iterator_to_string(islice(string, None)), string)
        self.assertEqual(iterator_to_string(islice(string, None, None)), string)
        
def compress_str(data, selectors) -> str:
    """
    Helper function to get a string from the call to `it.compress(data, selectors)`.
    Appends all the elements the iterator returns one after the other.
    """
    def iterator_to_str(iterator: it) -> str:
        if iterator is None:
            return ''
        result = ''
        for element in iterator:
            result = result + element
        return result
    return iterator_to_str(it.compress(data, selectors))


class TestCompress(unittest.TestCase):
    """Test class to test the `itertools.compress` function."""

    def test_example_documentation(self):
        """Example test cases from the documentation."""
        self.assertEqual(compress_str('ABCDEF', [1, 0, 1, 0, 1, 1]), 'ACEF')

    def test_expected_input(self):
        """Expected input (string and binary interger list of the same length) are given."""
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
        """Either the given list is None or a list containing Nones."""
        self.assertRaises(TypeError, lambda: compress_str('ABC', None))
        self.assertRaises(TypeError, lambda: compress_str('', None))
        self.assertEqual(compress_str('ABC', [None, None, None]), '')

    def test_boolean_list_shorter(self):
        """The given list is shorter than the length of the string."""
        self.assertEqual(compress_str('ABCDEF', [False, False]), '')
        self.assertEqual(compress_str('ABCDEF', [False, True]), 'B')
        self.assertEqual(compress_str('ABCDEF', [True, True]), 'AB')

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
        """A float list of same length as the string."""
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

    

def lessthanten(x):
    return x<10
def lessthanfive(x):
    return x<5
def greatthanneg(x):
    return x>-5
def greatthanpos(x):
    return x<-5

class testwhile(unittest.TestCase):
    
    def test_lessvalues(self):
        data1=[1,4,6,20,1,2,4,3,8]
        self.assertEqual(list(it.takewhile(lessthanten,data1)),[1,4,6])
        self.assertEqual(list(it.takewhile(lessthanfive,data1)),[1,4])
        self.assertEqual(list(it.dropwhile(lessthanten,data1)),[20,1,2,4,3,8])
        self.assertEqual(list(it.dropwhile(lessthanfive,data1)),[6,20,1,2,4,3,8])

    def test_morevalues(self):
        data2 = [2,4,7,9,3,4,1]
        self.assertEqual(list(it.takewhile(lessthanten,data2)),[2,4,7,9,3,4,1])
        self.assertEqual(list(it.takewhile(lessthanfive,data2)),[2,4])
        self.assertEqual(list(it.dropwhile(lessthanten,data2)),[])
        self.assertEqual(list(it.dropwhile(lessthanfive,data2)),[7,9,3,4,1])
    def test_nullvalues(self):
        data3=[]
        data4=[-1,0,1,2]
        self.assertEqual(list(it.takewhile(lessthanten,data3)),[])
        self.assertEqual(list(it.takewhile(lessthanfive,data3)),[])
        self.assertEqual(list(it.dropwhile(lessthanten,data3)),[])
        self.assertEqual(list(it.dropwhile(lessthanfive,data3)),[])
        self.assertEqual(list(it.takewhile(greatthanpos,data4)),[])
        self.assertEqual(list(it.dropwhile(greatthanneg,data4)),[])

    def test_negativevalues(self):
        data4 = [-3,-5,-7,-10,-1,-3,-5]
        self.assertEqual(list(it.takewhile(greatthanneg,data4)),[-3])
        self.assertEqual(list(it.dropwhile(greatthanneg,data4)),[-5,-7,-10,-1,-3,-5])


    def test_float(self):
        data7 = [1.1,3.8,4.6,5.1,10.15,1.5,8.5]
        self.assertEqual(list(it.takewhile(lessthanten,data7)),[1.1,3.8,4.6,5.1])
        self.assertEqual(list(it.takewhile(lessthanfive,data7)),[1.1,3.8,4.6])
        self.assertEqual(list(it.dropwhile(lessthanten,data7)),[10.15,1.5,8.5])
        self.assertEqual(list(it.dropwhile(lessthanfive,data7)),[5.1,10.15,1.5,8.5])
    
    def test_mixed(self):
        data8 = [-1,-2.5,0,3,4.99,99.99,100.1,5599,777]
        self.assertEqual(list(it.takewhile(lessthanten,data8)),[-1,-2.5,0,3,4.99])
        self.assertEqual(list(it.takewhile(lessthanten,data8)),[-1,-2.5,0,3,4.99])
    
    def test_string(self):
        self.assertEqual(list(it.takewhile(lambda c : c != 'I', 'ASYNIOL')),['A', 'S', 'Y', 'N'])
        self.assertEqual(list(it.dropwhile(lambda c : c != 'I', 'ASYNIOL')),['I', 'O', 'L'])
        self.assertEqual(list(it.takewhile(lambda c : c.lower() not in "aeiou", 'baroplane')),['b'])
        self.assertEqual(list(it.dropwhile(lambda c : c.lower() not in "aeiou", 'aeroplane')),['a', 'e', 'r', 'o', 'p', 'l', 'a', 'n', 'e'])
        
    def test_typeerror(self):
        self.assertRaises(TypeError, it.takewhile)
        self.assertRaises(TypeError, it.dropwhile)
        self.assertRaises(TypeError, it.takewhile, operator)
        self.assertRaises(TypeError, it.takewhile, operator.pow, [(10,5)], None)
        self.assertRaises(TypeError, it.dropwhile, operator)
        self.assertRaises(TypeError, it.dropwhile, operator.pow, [(10,5)], None)    

class testchainfrom(unittest.TestCase):
    
    def test_shortlist(self):
        posList1 = ['789','101112']
        posList2 = ['10,11,12']
        self.assertEqual(list(it.chain.from_iterable(posList1)), ['7', '8', '9', '1', '0', '1', '1', '1', '2'])#test with comma excluded in the float value
        self.assertEqual(list(it.chain.from_iterable(posList2)), ['1', '0', ',', '1', '1', ',', '1', '2'])#test with comma included

    def test_string(self):
        self.assertEqual(list(it.chain.from_iterable(['abc', 'def'])), ['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(list(it.chain.from_iterable(['abc'])), ['a', 'b', 'c'])

    def test_empty_spaces(self):    
        self.assertEqual(list(it.chain.from_iterable([''])), [])
        self.assertEqual(list(it.chain.from_iterable(['a b c'])), ['a', ' ', 'b', ' ', 'c'])
        self.assertEqual(list(it.chain.from_iterable(['a b c'])), ['a', ' ', 'b', ' ', 'c'])
    
    def test_mixed(self):
        self.assertEqual(list(it.chain.from_iterable(['1asd91234,mx..'])), ['1', 'a', 's', 'd', '9', '1', '2', '3', '4', ',', 'm', 'x', '.', '.'])
       
       
    def test_typeerror(self):
        self.assertRaises(TypeError, list, it.chain.from_iterable([2, 3]))   



class TestCode(unittest.TestCase):

    def test_permutest(self):
        # self.assertEqual(code.permutest(sending value),result)
        # self.assertEqual(code.permutest(1,2,3,4,5), )
        self.assertEqual(code_anwar.permutest('ABC'),
                         [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'),
                          ('C', 'B', 'A')])
        self.assertEqual(code_anwar.permutest('A C'),
                         [('A', ' ', 'C'), ('A', 'C', ' '), (' ', 'A', 'C'), (' ', 'C', 'A'), ('C', 'A', ' '),
                          ('C', ' ', 'A')])
        self.assertEqual(code_anwar.permutest('A'), [])
        self.assertEqual(code_anwar.permutest('123'),
                         [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'),
                          ('3', '2', '1')])
        self.assertEqual(code_anwar.permutest(['A', 'B', 'C']),
                         [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'),
                          ('C', 'B', 'A')])
        self.assertEqual(code_anwar.permutest([1, 2, 3]), [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)])
        self.assertEqual(code_anwar.permutest([-1, 2, -3]),
                         [(-1, 2, -3), (-1, -3, 2), (2, -1, -3), (2, -3, -1), (-3, -1, 2), (-3, 2, -1)])
        self.assertEqual(code_anwar.permutest([-1, 2, 'a', 0, '']),
                         [(-1, 2, 'a'), (-1, 2, 0), (-1, 2, ''), (-1, 'a', 2), (-1, 'a', 0), (-1, 'a', ''), (-1, 0, 2),
                          (-1, 0, 'a'), (-1, 0, ''), (-1, '', 2), (-1, '', 'a'), (-1, '', 0), (2, -1, 'a'), (2, -1, 0),
                          (2, -1, ''), (2, 'a', -1), (2, 'a', 0), (2, 'a', ''), (2, 0, -1), (2, 0, 'a'), (2, 0, ''),
                          (2, '', -1), (2, '', 'a'), (2, '', 0), ('a', -1, 2), ('a', -1, 0), ('a', -1, ''),
                          ('a', 2, -1), ('a', 2, 0), ('a', 2, ''), ('a', 0, -1), ('a', 0, 2), ('a', 0, ''),
                          ('a', '', -1), ('a', '', 2), ('a', '', 0), (0, -1, 2), (0, -1, 'a'), (0, -1, ''), (0, 2, -1),
                          (0, 2, 'a'), (0, 2, ''), (0, 'a', -1), (0, 'a', 2), (0, 'a', ''), (0, '', -1), (0, '', 2),
                          (0, '', 'a'), ('', -1, 2), ('', -1, 'a'), ('', -1, 0), ('', 2, -1), ('', 2, 'a'), ('', 2, 0),
                          ('', 'a', -1), ('', 'a', 2), ('', 'a', 0), ('', 0, -1), ('', 0, 2), ('', 0, 'a')])
        # check for empty input, check for empty lists as Input.
        self.assertEqual(code_anwar.permutest(''), [])
        self.assertEqual(code_anwar.permutest('0'), [])
        # self.assertEqual(code.permutest(0), 0)                   #TypeError: 'int' object is not iterable
        self.assertEqual(code_anwar.permutest([0]), [])
        self.assertEqual(code_anwar.permutest([]), [])

    def test_grouptest(self):
        self.assertEqual(code_anwar.grouptest(['mouse', 'monkey', 'donkey', 'dog', 'cow', 'cat', 'bat']),
                         ([['bat'], ['cat', 'cow'], ['dog', 'donkey'], ['monkey', 'mouse']]))
        self.assertEqual(code_anwar.grouptest(
            [('Male', 'Rahim', '28'), ('FeMale', 'kajsa', '18'), ('Male', 'Kanan', '25'), ('FeMale', 'Tina', '31')]),
                         [[('FeMale', 'Tina', '31'), ('FeMale', 'kajsa', '18')],
                          [('Male', 'Kanan', '25'), ('Male', 'Rahim', '28')]])
        self.assertEqual(code_anwar.grouptest([[1, 2, 3, 4], [1, 5, 4], [4, 9], [3, 4], [3, 5, 6, 4]]),
                         ([[[1, 2, 3, 4], [1, 5, 4]], [[3, 4], [3, 5, 6, 4]], [[4, 9]]]))
        self.assertEqual(code_anwar.grouptest([[-1], [-12], [-32], [22], [0], [23], [-23], [-1]]),
                         ([[[-32]], [[-23]], [[-12]], [[-1], [-1]], [[0]], [[22]], [[23]]]))
        # check for empty input, check for empty lists as Input.
        self.assertEqual(code_anwar.grouptest([[0], [], [0], []]), (
        [[[0], [0]]]))  # lamda 0 is the first letter of word or number list #IndexError: list index out of range
        self.assertEqual(code_anwar.grouptest(['', '', '']),
                         [])  # lamda 0 is the first letter of word or number list #IndexError: list index out of range

    def test_fitest(self):
        self.assertEqual(code_anwar.fitest([2, -6, -9, 0, -3, 8, 5]), [2, -6, -9, -3, 8, 5])
        self.assertEqual(code_anwar.fitest([2, -6, -7, 0, -3, 8, 5]), [2, 8, 5])
        self.assertEqual(code_anwar.fitest([2, -6, -4, 0, -3, 8, 5]), [-6, -4, -3])
        self.assertEqual(code_anwar.fitest([-3, 0, 4, 8, 2]), [-3, 4, 8, 2])

        self.assertEqual(code_anwar.fitest(['apple', 'banana', 'orange', 'mango', 'lemon', 'lichy']),
                         ['banana', 'orange', 'mango', 'lemon', 'lichy'])
        self.assertEqual(code_anwar.fitest(['apple', 'banana', 'orange', 'mango', 'lemon']), ['lemon'])
        self.assertEqual(code_anwar.fitest(['apple', '', 'orange', '', 'lemon']), [])
        self.assertEqual(code_anwar.fitest(['apple', '', 'orange', 'mango', 'lemon']), ['apple', 'orange', 'mango', 'lemon'])
        # check for empty input, check for empty lists as Input.
        self.assertEqual(code_anwar.fitest([]), [])
        self.assertEqual(code_anwar.fitest(['']), [''])


class TestIterToolsB(unittest.TestCase):
	"""Functionsfortestingtheextractionofauthornames.
	NotethattherulesforextractingitertoolsBauthornamesisactually
	quitecomplicated.Asthesetestcasesillustrate.Ihaven’t
	implementedallthecases."""
	def setUp(self):
		self.string1="ABCD"
		self.string2="ABCD "
		self.numList1=[1,2,3,4,5,6,7]
		self.numList2=[1,2,2,3,3,4,5]
		self.multiList2=[2,'',(2,4),"Hello",5]

	def testcombinations(self):
		
		numCombs = len(list(it.combinations(self.string1,2)))
		self.assertEqual(numCombs,6) # testing a string
		numCombs = len(list(it.combinations(self.string2,2)))
		self.assertEqual(numCombs,10) # testing a string with a space		
		numCombs = len(list(it.combinations(self.numList1,4)))
		self.assertEqual(numCombs,35) # testing a list of numbers
		numCombs = len(list(it.combinations(self.numList2,2)))
		self.assertEqual(numCombs,21) # testing a list of numbers with repeated elements
		numCombs = len(list(it.combinations(self.multiList2,2)))
		self.assertEqual(numCombs,10) # testing a polymorphic list

		self.assertRaises(TypeError, it.combinations, self.string1) # testing TypeError: 'r' argument is missing
		self.assertRaises(TypeError, it.combinations, self.string1, 3, 6) # testing TypeError: extra argument
		self.assertRaises(TypeError, it.combinations, 5) # testing TypeError: first argument is not an iterable
		self.assertRaises(TypeError, it.combinations) # testing TypeError: no argument given
		self.assertRaises(ValueError, it.combinations, self.string1, -3) # testing ValueError: 'r' argument is a negative number
		self.assertRaises(MemoryError, it.combinations, self.string1, 3**20) #testing MemoryError: operation runs out of memory because the groups are too large

		

	def testcombinationsWithRep(self):
		
		numCombs = len(list(it.combinations_with_replacement(self.string1,2)))
		self.assertEqual(numCombs,10) # testing a string
		numCombs = len(list(it.combinations_with_replacement(self.string2,2)))
		self.assertEqual(numCombs,15) # testing a string with a space
		numCombs = len(list(it.combinations_with_replacement(self.numList1,4)))
		self.assertEqual(numCombs,210) # testing a list of nummbers
		numCombs = len(list(it.combinations_with_replacement(self.numList2,2)))
		self.assertEqual(numCombs,28) # testing a list of numbers with repeated elements
		numCombs = len(list(it.combinations_with_replacement(self.multiList2,2)))
		self.assertEqual(numCombs,15) # testing a polymorphic list

		self.assertRaises(TypeError, it.combinations_with_replacement, self.string1) # testing TypeError: 'r' argument is missing
		self.assertRaises(TypeError, it.combinations_with_replacement, self.string1, 3, 6) # testing TypeError: extra argument
		self.assertRaises(TypeError, it.combinations_with_replacement, 5) # testing TypeError: first argument is not an iterable
		self.assertRaises(TypeError, it.combinations_with_replacement) # testing TypeError: no argument given
		self.assertRaises(ValueError, it.combinations_with_replacement, self.string1, -3) # testing ValueError: 'r' argument is a negative number
		self.assertRaises(MemoryError, it.combinations_with_replacement, self.string1, 3**20) # testing MemoryError: operation runs out of memory because the groups are too large


	def testCycle(self):
		self.assertEqual(list(it.islice(cycle(self.string1), 10)), list("ABCDABCDAB")) # testing a string
		self.assertEqual(list(it.islice(cycle(self.numList1), 13)), [1,2,3,4,5,6,7,1,2,3,4,5,6]) # testing a list of nummbers
		self.assertEqual(list(it.islice(cycle(self.multiList2), 8)), [2,'',(2,4),"Hello",5,2,'',(2,4)]) # testing a polymorphic list
		self.assertEqual(list(it.islice(cycle(""), 4)), list("")) # testing with an empty string and multiple cycles
		self.assertEqual(list(it.islice(cycle(self.string1), 0)), list("")) #testing a string with 0 cycles

		self.assertRaises(TypeError, cycle, 3) # testing TypeError: argument is not an iterable
		self.assertRaises(TypeError, cycle, self.string1, 4) #testing TypeError: extra argument
		self.assertRaises(TypeError, cycle) # testing TypeError: no argument given

if __name__ == '__main__':
    unittest.main()
