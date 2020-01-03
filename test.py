import unittest
from itertools import *
import numpy as np
from decimal import Decimal
from fractions import Fraction
import operator

def lzip(*args):
    return list(zip(*args))

	
class Test_itertools(unittest.TestCase):
	'''
	Count:
	Make an iterator that returns evenly spaced values starting with number start. 
	Often used as an argument to map() to generate consecutive data points. 
	Also, used with zip() to add sequence numbers.
	First test 	tests for default method call without input
	Second test	tests for method call with positive offset
	Third test	tests for method call with negative offset
	Fourth test 	tests for method call with offset and positive counter
	Fifth test	tests for method call with offset and negative counter
	Sixth test	tests for method call with offset and 0-counter
	Seventh test	tests for method call with non-integer offset and non-integer counter
	Eighth test	tests for too many arguments
	Nineth test	tests for non-numerical arguments
	Tenth test	tests for mixed-type arguments
	'''
	def test_count(self):
		# Correct uses
		self.assertEqual(lzip('abc',  count()), [('a', 0), ('b', 1), ('c', 2)])
		self.assertEqual(lzip('abc',  count(4)), [('a', 4), ('b', 5), ('c', 6)])
		self.assertEqual(lzip('abc',  count(-10)), [('a', -10), ('b', -9), ('c', -8)])
		self.assertEqual(lzip('abc',  count(4,2)), [('a', 4), ('b', 6), ('c', 8)])
		self.assertEqual(lzip('abc',  count(4,-1)), [('a', 4), ('b', 3), ('c', 2)])
		self.assertEqual(lzip('abc',  count(4,0)), [('a', 4), ('b', 4), ('c', 4)])
		self.assertEqual(lzip('abc',  count(1.5,0.25)), [('a', 1.5), ('b', 1.75), ('c', 2)])
		# Type Errors
		self.assertRaises(TypeError,  count, 2,3,4)
		self.assertRaises(TypeError,  count, 'a')
		self.assertRaises(TypeError,  count, 2, 'c')
		
		
		
	'''
	zip_longest:
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
			
			self.assertEqual(list(zip_longest(*args)), target)
			self.assertEqual(list(zip_longest(*args, **{})), target)
			
			# replace None with fillvalue manually
			target = [tuple((e is None and 'X' or e) for e in t) for t in target]   
			self.assertEqual(list(zip_longest(*args, **dict(fillvalue='X'))), target)
		
		self.assertEqual(list(zip_longest()), list(zip()))
		self.assertEqual(list(zip_longest([])), list(zip([])))
	
		# Type Errors
		self.assertRaises(TypeError, zip_longest, '12345678', 45)
		self.assertRaises(TypeError, zip_longest, 3)
		self.assertRaises(TypeError, zip_longest, None)

		
	'''
	Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).
	If func is supplied, it should be a function of two arguments. 
	Elements of the input iterable may be any type that can be accepted as arguments to func. (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)
	Usually, the number of elements output matches the input iterable. 
	However, if the keyword argument initial is provided, the accumulation leads off with the initial value so that the output has one more element than the input iterable.
	First test	tests for strings 
	Tests for different type of numerical values: int, complex, decimal, fraction
	Tests for empty lists, lists with only one entry, negative integers and floats with and without the initial keyword 
	Tests the operator-keyword
	Type Error Tests:
		test for too little arguments
		test for too many arguments
		test for mixed-type arguments
	'''
	def test_accumulate(self):	
		self.assertEqual(list(accumulate('abcd', initial = None)),['a', 'ab', 'abc','abcd'])		
		for typ in int, complex, Decimal, Fraction:                
			self.assertEqual(
				list(accumulate(map(typ, range(10)))),
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
				
			self.assertEqual(list(accumulate([*args], initial=None)), target)
			self.assertEqual(list(accumulate([*args], initial=init)), target_offset)

			
			
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
			self.assertEqual(list(accumulate([*args], operator.mul, initial = None)), target)		
			self.assertEqual(list(accumulate([*args], operator.mul, initial=init)), target_offset)	
			
			
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
			self.assertEqual(list(accumulate([*args], max, initial = None)), target)	
			self.assertEqual(list(accumulate([*args], max, initial=init)), target_offset)	

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
			self.assertEqual(list(accumulate([*args], min, initial = None)), target)		
			self.assertEqual(list(accumulate([*args], min, initial=init)), target_offset)	

		# Type Errors	
		self.assertRaises(TypeError, accumulate) 							
		self.assertRaises(TypeError, accumulate, [1,2,3,], operator.mul, 2) 
		self.assertRaises(TypeError, list, accumulate([1, 'a']))		
