import unittest
from itertools import *


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

        result = list(product(self.posList2))
        self.assertEqual(result,([(10,),(11,),(12,)])) #Testing list of positive values without repeat argument           

        result = list(product(self.negList1,self.emptyList1))
        self.assertEqual(result,([])) #Testing list of negative values with empty list and without repeat argument       

        result = list(product(self.floatList1,self.strList1,repeat=1))
        self.assertEqual(result,([(10.15, 'Hello'), (1.5, 'Hello'), (8.5, 'Hello')])) #Testing list of float and string values with repaet argument
       
        result = list(product(self.floatList2,self.strList2,self.emptyList1,repeat=1))
        self.assertEqual(result,([])) #Testing multiple iterable list with empty list 
        
        result = list(product(self.strValue1,repeat=2))
        self.assertEqual(result,([('H', 'H'), ('H', 'i'), ('i', 'H'), ('i', 'i')])) #Testing string value with repeat argument
        
        result = list(product())
        self.assertEqual(result,([()])) #Testing without aruguments          

        result = list(product(self.multiList1,repeat=1))
        self.assertEqual(result,([(8.9,), (-8,), ((1, 4),), ('Welcome!',), (5,), ('',), (-20,)])) #Testing polymorphic list
       
        result = list(product(*self.strList2))
        self.assertEqual(result,([('W',), ('o',), ('r',), ('l',), ('d',)])) #Testing list of positive values without repeat argument
        
        range1 = list(product(range(5)))
        self.assertEqual(range1,([(0,), (1,), (2,),(3,),(4,)])) #Testing for range of positive value         

        self.assertRaises(TypeError,product,self.intValue,repeat=2) #testing TypeError: integer object is not an iterable
        self.assertRaises(TypeError,product,self.strValue1,repeat=2.5) #testing TypeError: integer argument expected, got float        
        self.assertRaises(TypeError,product,self.strValue1,repeat='12')  # Testing TypeError: 'string' object cannot be interpreted as an integer
        self.assertRaises(OverflowError,product,self.strList2,repeat=8**60) #testing OverflowError: Python int too large to convert to C ssize_t


        

    def test_for_chain(self):
       
        chainlist = list(chain(self.posList1,self.posList2))
        self.assertListEqual(chainlist, [7,8,9,10,11,12]) #Testing with list of positive values        

        chainlist = list(chain(self.negList1,self.negList2))
        self.assertListEqual(chainlist, [-1,-2,-3,-4,-10,-11,-12]) #Testing with list of negative values        

        chainlist = list(chain(self.posList1,self.negList2)) #Testing with list of positive and negative values
        self.assertListEqual(chainlist,[7,8,9,-10,-11,-12])          
        
        chainlist = list(chain(self.posList1,self.posList1)) #Testing for same list/single list
        self.assertListEqual(chainlist, [7,8,9,7,8,9])        

        chainlist = list(chain(self.posList1,self.floatList2)) #Testing with list of positive and decimal values
        self.assertListEqual(chainlist,[7,8,9,-1.0,-2.5,99.99,100.1,5599,777])
        
        chainlist = list(chain(self.strList1,self.strList2)) #Testing for list of string values
        self.assertListEqual(chainlist,['Hello', 'World'])
        
        chainlist = list(chain())
        self.assertListEqual(chainlist,[]) #Testing without argument

        chainlist = list(chain(self.strList1,chain(self.negList2,chain(self.floatList1)))) #Testing for multiple chain()
        self.assertListEqual(chainlist,['Hello', -10, -11, -12, 10.15, 1.5, 8.5])
                
        chainMixedList = list(chain(self.strList1,self.negList1,self.posList2,self.floatList2)) #Testing with list of mixed values
        self.assertListEqual(chainMixedList,['Hello',-1,-2,-3,-4,10,11,12,-1.0,-2.5,99.99,100.1,5599,777])        

        emptyList = list(chain(self.emptyList1,self.emptyList2)) #Testing for empty list
        self.assertListEqual(emptyList, [])
        
        multiList = list(chain(self.multiList1,self.emptyList2))
        self.assertListEqual(multiList, [8.9,-8,(1, 4),'Welcome!',5,'',-20]) #Testing multi value list and empty list        

        stringValue = (list(chain(self.strValue1,self.strValue1)))
        self.assertListEqual(stringValue,['H','i','H','i']) #Testing for string value           
      

               
    

    def test_for_repeat(self):

        result = list(repeat(self.strValue1,2))       
        self.assertEqual(result,['Hi','Hi']) #Testing with string      

        result = list(repeat(self.intValue,5))       
        self.assertEqual(result,[12,12,12,12,12]) #Testing with integer             

        result = list(repeat(self.strList1,5))       
        self.assertEqual(result,[['Hello'],['Hello'],['Hello'],['Hello'],['Hello']]) #Testing with string list         

        result = list(repeat("",3))
        self.assertEqual(result,['', '', '']) #Testing with empty string        

        result = list(repeat(self.emptyList1,3))
        self.assertEqual(result,[[],[],[]]) #Testing with empty List         

        result = list(repeat(self.strValue1, 0))
        self.assertEqual(result,[]) #testing a string with 0 cycles         

        result = list(repeat(self.multiList1, 2))
        self.assertEqual(result,[[8.9, -8, (1, 4), 'Welcome!', 5, '', -20], [8.9, -8, (1, 4), 'Welcome!', 5, '', -20]]) ##testing a list with different type of values
    
        result = list(repeat(self.negList2, 2**2))
        self.assertEqual(result,[[-10, -11, -12], [-10, -11, -12], [-10, -11, -12], [-10, -11, -12]]) #testing with list of negative values 
        

        self.assertRaises(TypeError, repeat) # testing TypeError: no argument given
        self.assertRaises(TypeError, repeat,self.intValue,self.strValue1,3) #Testing Type Error with extra argument
        self.assertRaises(TypeError, repeat,self.intValue,5.7) # testing typeError:- integer argument expected, got float
        self.assertRaises(OverflowError,repeat,self.strList2,4**40) #testing OverflowError: Python int too large to convert to C ssize_t


if __name__ == '__main__':
    unittest.main()