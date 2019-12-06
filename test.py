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
	Make an iterator that returns evenly spaced values starting with number start. Often used as an argument to map() to generate consecutive data points. Also, used with zip() to add sequence numbers.
	'''
	def test_count(self):
		#self.assertEqual(itertools.count(0))
		self.assertEqual(lzip('abc',  count()), [('a', 0), ('b', 1), ('c', 2)])
		self.assertEqual(lzip('abc',  count(4)), [('a', 4), ('b', 5), ('c', 6)])
		self.assertEqual(lzip('abc',  count(4,2)), [('a', 4), ('b', 6), ('c', 8)])
		self.assertEqual(lzip('abc',  count(4,0)), [('a', 4), ('b', 4), ('c', 4)])

		self.assertEqual(lzip('abc',  count(4,-1)), [('a', 4), ('b', 3), ('c', 2)])

		self.assertEqual(lzip('abc',  count(1.5,0.25)), [('a', 1.5), ('b', 1.75), ('c', 2)])
		self.assertEqual(lzip('abc',  count(-10)), [('a', -10), ('b', -9), ('c', -8)])
		self.assertEqual(lzip('abc',  count(-1)), [('a', -1), ('b', 0), ('c', 1)])
		
		
		self.assertEqual(list( islice( count(100), 10)), list(range(100, 100+10)))
		self.assertEqual(list( islice( count(100,2), 5)), (list(islice(range(100, 200, 2),5))))

		### Type Errors
		self.assertRaises(TypeError,  count, 2,3,4)
		self.assertRaises(TypeError,  count, 'a', 'b', 'c')
		self.assertRaises(TypeError,  count, 'a')
		self.assertRaises(TypeError,  count, 2, 'c')
		#typeerror, overflowerror, stopiteration error
		#empty lists, floats, 
		
		
	'''
	Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted. 
	'''
	
	def test_zip_longest(self):
		#test for different number of entries, different values and different length of iterables
		for args in [
			['abc'],
			[range(9), 'abc'],
			['abc', range(4)],
			[range(789), range(1987,2100), range(100,150)],
			[range(1000), range(0), range(-100,150), range(120), range(420)],
			[range(1000), range(0), range(100,150), range(-120,120), range(420), range(0)],
			]:
			#generate test result to check for Equal
			target = [tuple([arg[i] if i < len(arg) else None for arg in args])
					  for i in range(max(map(len, args)))]
			
			self.assertEqual(list(zip_longest(*args)), target)
			self.assertEqual(list(zip_longest(*args, **{})), target)
			#generate test result with fillvalue to check for Equal
			target = [tuple((e is None and 'X' or e) for e in t) for t in target]   # Replace None fills with 'X'
			self.assertEqual(list(zip_longest(*args, **dict(fillvalue='X'))), target)
		
		#check for empty input, check for empty lists as Input.
		self.assertEqual(list(zip_longest()), list(zip()))
		self.assertEqual(list(zip_longest([])), list(zip([])))
	
		### Type Errors
		#check for inadequate entries aka non iterables.
		self.assertRaises(TypeError, zip_longest, (1,2,3,4), 'a', 2)
		self.assertRaises(TypeError, zip_longest, '12345678', 'abcdefghijkl', 45)
		self.assertRaises(TypeError, zip_longest, 3,4)
		self.assertRaises(TypeError, zip_longest, None)

		
	'''
	Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument).

	If func is supplied, it should be a function of two arguments. Elements of the input iterable may be any type that can be accepted as arguments to func. (For example, with the default operation of addition, elements may be any addable type including Decimal or Fraction.)

	Usually, the number of elements output matches the input iterable. However, if the keyword argument initial is provided, the accumulation leads off with the initial value so that the output has one more element than the input iterable.
	'''
	def test_accumulate(self):
		self.assertEqual(list(accumulate('abcd')),['a', 'ab', 'abc','abcd'])		#strings
		self.assertEqual(list(accumulate([1, 2, 3], initial=None)), [1, 3, 6])		#initial keyword set to None (default)
		init = 100			
		#############
		# test numbers
		# test initial keyword
		# test different operators
		#############
		for args in [
			[],																		#empty lists
			[7],																	#only one entry
			np.arange(10), 															#integer
			np.arange(-10,0),														#negative integers
			np.arange(0.0, 1.0, 0.1)												# floats
			]:
			
			#generate test result to check for Equal
			target = []
			target_offset = [init]
			current = 0
			current_offset = init
			for i in args:
				current += i
				current_offset += i
				target.append(current)	
				target_offset.append(current_offset)
			self.assertEqual(list(accumulate([*args])), target)
			self.assertEqual(list(accumulate([*args], initial=init)), target_offset)

			
			
			######################
			### with func operator
			######################
			target = []
			target_offset = [init]
			current = 1
			current_offset = init
			for i in args:
				current *= i
				current_offset *= i
				target.append(current)	
				target_offset.append(current_offset)
			self.assertEqual(list(accumulate([*args], operator.mul)), target)						# check multiplication
			self.assertEqual(list(accumulate([*args], operator.mul, initial=init)), target_offset)	#check multi with offset
			
			
			target = []
			target_offset = [init]
			current = -10000000
			current_offset = init
			for i in args:
				if i > current: current = i 
				if i > current_offset: current_offset = i
				target.append(current)
				target_offset.append(current_offset)
			self.assertEqual(list(accumulate([*args], max)), target)					# check max operator
			self.assertEqual(list(accumulate([*args], max, initial=init)), target_offset)	#check max with offset

			current = 10000000
			target = []
			current_offset = init
			target_offset = [init]
			for i in args:
				if i < current: current = i 
				if i < current_offset: current_offset = i
				target.append(current)
				target_offset.append(current_offset)
			self.assertEqual(list(accumulate([*args], min)), target)					#check min operator
			self.assertEqual(list(accumulate([*args], min, initial=init)), target_offset)	#check min with offset

			
		
		#test for more different types:
		for typ in int, complex, Decimal, Fraction:                
			self.assertEqual(
				list(accumulate(map(typ, range(10)))),
				list(map(typ, [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])))
				
				
		######################
		### Raises Errors
		######################
		self.assertRaises(TypeError, accumulate) 							#too little args
		self.assertRaises(TypeError, accumulate, [1,2,3,], operator.mul, 2) # too many args
		#	self.assertRaises(TypeError, accumulate, ([1],'a'))
		# self.assertRaises(TypeError, accumulate, ['a',1, 'b'])			#different types

		# self.assertRaises(TypeError, accumulate, [1,2,3], 12345)			# wrong kwd arg
		self.assertRaises(TypeError, list, accumulate([1, []]))     		# args that are not combinable
		self.assertRaises(TypeError, list, accumulate([1, 'a']))			# different type of args
		

