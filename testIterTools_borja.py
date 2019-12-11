import unittest
from itertools import *

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

	def testCombinations(self):
		
		numCombs = len(list(combinations(self.string1,2)))
		self.assertEqual(numCombs,6) # testing a string
		numCombs = len(list(combinations(self.string2,2)))
		self.assertEqual(numCombs,10) # testing a string with a space		
		numCombs = len(list(combinations(self.numList1,4)))
		self.assertEqual(numCombs,35) # testing a list of numbers
		numCombs = len(list(combinations(self.numList2,2)))
		self.assertEqual(numCombs,21) # testing a list of numbers with repeated elements
		numCombs = len(list(combinations(self.multiList2,2)))
		self.assertEqual(numCombs,10) # testing a polymorphic list

		self.assertRaises(TypeError, combinations, self.string1) # testing TypeError: 'r' argument is missing
		self.assertRaises(TypeError, combinations, self.string1, 3, 6) # testing TypeError: extra argument
		self.assertRaises(TypeError, combinations, 5) # testing TypeError: first argument is not an iterable
		self.assertRaises(TypeError, combinations) # testing TypeError: no argument given
		self.assertRaises(ValueError, combinations, self.string1, -3) # testing ValueError: 'r' argument is a negative number
		self.assertRaises(MemoryError, combinations, self.string1, 3**20) #testing MemoryError: operation runs out of memory because the groups are too large

		

	def testCombinationsWithRep(self):
		
		numCombs = len(list(combinations_with_replacement(self.string1,2)))
		self.assertEqual(numCombs,10) # testing a string
		numCombs = len(list(combinations_with_replacement(self.string2,2)))
		self.assertEqual(numCombs,15) # testing a string with a space
		numCombs = len(list(combinations_with_replacement(self.numList1,4)))
		self.assertEqual(numCombs,210) # testing a list of nummbers
		numCombs = len(list(combinations_with_replacement(self.numList2,2)))
		self.assertEqual(numCombs,28) # testing a list of numbers with repeated elements
		numCombs = len(list(combinations_with_replacement(self.multiList2,2)))
		self.assertEqual(numCombs,15) # testing a polymorphic list

		self.assertRaises(TypeError, combinations_with_replacement, self.string1) # testing TypeError: 'r' argument is missing
		self.assertRaises(TypeError, combinations_with_replacement, self.string1, 3, 6) # testing TypeError: extra argument
		self.assertRaises(TypeError, combinations_with_replacement, 5) # testing TypeError: first argument is not an iterable
		self.assertRaises(TypeError, combinations_with_replacement) # testing TypeError: no argument given
		self.assertRaises(ValueError, combinations_with_replacement, self.string1, -3) # testing ValueError: 'r' argument is a negative number
		self.assertRaises(MemoryError, combinations_with_replacement, self.string1, 3**20) # testing MemoryError: operation runs out of memory because the groups are too large


	def testCycle(self):
		self.assertEqual(list(islice(cycle(self.string1), 10)), list("ABCDABCDAB")) # testing a string
		self.assertEqual(list(islice(cycle(self.numList1), 13)), [1,2,3,4,5,6,7,1,2,3,4,5,6]) # testing a list of nummbers
		self.assertEqual(list(islice(cycle(self.multiList2), 8)), [2,'',(2,4),"Hello",5,2,'',(2,4)]) # testing a polymorphic list
		self.assertEqual(list(islice(cycle(""), 4)), list("")) # testing with an empty string and multiple cycles
		self.assertEqual(list(islice(cycle(self.string1), 0)), list("")) #testing a string with 0 cycles

		self.assertRaises(TypeError, cycle, 3) # testing TypeError: argument is not an iterable
		self.assertRaises(TypeError, cycle, self.string1, 4) #testing TypeError: extra argument
		self.assertRaises(TypeError, cycle) # testing TypeError: no argument given

if __name__ == '__main__':
	unittest.main()