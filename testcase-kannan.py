import unittest
from itertools import takewhile,dropwhile,chain
import operator
    

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
        self.assertEqual(list(takewhile(lessthanten,data1)),[1,4,6])
        self.assertEqual(list(takewhile(lessthanfive,data1)),[1,4])
        self.assertEqual(list(dropwhile(lessthanten,data1)),[20,1,2,4,3,8])
        self.assertEqual(list(dropwhile(lessthanfive,data1)),[6,20,1,2,4,3,8])

    def test_morevalues(self):
        data2 = [2,4,7,9,3,4,1]
        self.assertEqual(list(takewhile(lessthanten,data2)),[2,4,7,9,3,4,1])
        self.assertEqual(list(takewhile(lessthanfive,data2)),[2,4])
        self.assertEqual(list(dropwhile(lessthanten,data2)),[])
        self.assertEqual(list(dropwhile(lessthanfive,data2)),[7,9,3,4,1])
    def test_nullvalues(self):
        data3=[]
        data4=[-1,0,1,2]
        self.assertEqual(list(takewhile(lessthanten,data3)),[])
        self.assertEqual(list(takewhile(lessthanfive,data3)),[])
        self.assertEqual(list(dropwhile(lessthanten,data3)),[])
        self.assertEqual(list(dropwhile(lessthanfive,data3)),[])
        self.assertEqual(list(takewhile(greatthanpos,data4)),[])
        self.assertEqual(list(dropwhile(greatthanneg,data4)),[])

    def test_negativevalues(self):
        data4 = [-3,-5,-7,-10,-1,-3,-5]
        self.assertEqual(list(takewhile(greatthanneg,data4)),[-3])
        self.assertEqual(list(dropwhile(greatthanneg,data4)),[-5,-7,-10,-1,-3,-5])


    def test_float(self):
        data7 = [1.1,3.8,4.6,5.1,10.15,1.5,8.5]
        self.assertEqual(list(takewhile(lessthanten,data7)),[1.1,3.8,4.6,5.1])
        self.assertEqual(list(takewhile(lessthanfive,data7)),[1.1,3.8,4.6])
        self.assertEqual(list(dropwhile(lessthanten,data7)),[10.15,1.5,8.5])
        self.assertEqual(list(dropwhile(lessthanfive,data7)),[5.1,10.15,1.5,8.5])
    
    def test_mixed(self):
        data8 = [-1,-2.5,0,3,4.99,99.99,100.1,5599,777]
        self.assertEqual(list(takewhile(lessthanten,data8)),[-1,-2.5,0,3,4.99])
        self.assertEqual(list(takewhile(lessthanten,data8)),[-1,-2.5,0,3,4.99])
    
    def test_string(self):
        self.assertEqual(list(takewhile(lambda c : c != 'I', 'ASYNIOL')),['A', 'S', 'Y', 'N'])
        self.assertEqual(list(dropwhile(lambda c : c != 'I', 'ASYNIOL')),['I', 'O', 'L'])
        self.assertEqual(list(takewhile(lambda c : c.lower() not in "aeiou", 'baroplane')),['b'])
        self.assertEqual(list(dropwhile(lambda c : c.lower() not in "aeiou", 'aeroplane')),['a', 'e', 'r', 'o', 'p', 'l', 'a', 'n', 'e'])
        
    def test_typeerror(self):
        self.assertRaises(TypeError, takewhile)
        self.assertRaises(TypeError, dropwhile)
        self.assertRaises(TypeError, takewhile, operator)
        self.assertRaises(TypeError, takewhile, operator.pow, [(10,5)], None)
        self.assertRaises(TypeError, dropwhile, operator)
        self.assertRaises(TypeError, dropwhile, operator.pow, [(10,5)], None)    

class testchainfrom(unittest.TestCase):
    
    def test_shortlist(self):
        posList1 = ['789','101112']
        posList2 = ['10,11,12']
        self.assertEqual(list(chain.from_iterable(posList1)), ['7', '8', '9', '1', '0', '1', '1', '1', '2'])#test with comma excluded in the float value
        self.assertEqual(list(chain.from_iterable(posList2)), ['1', '0', ',', '1', '1', ',', '1', '2'])#test with comma included

    def test_string(self):
        self.assertEqual(list(chain.from_iterable(['abc', 'def'])), ['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(list(chain.from_iterable(['abc'])), ['a', 'b', 'c'])

    def test_empty_spaces(self):    
        self.assertEqual(list(chain.from_iterable([''])), [])
        self.assertEqual(list(chain.from_iterable(['a b c'])), ['a', ' ', 'b', ' ', 'c'])
        self.assertEqual(list(chain.from_iterable(['a b c'])), ['a', ' ', 'b', ' ', 'c'])
    
    def test_mixed(self):
        self.assertEqual(list(chain.from_iterable(['1asd91234,mx..'])), ['1', 'a', 's', 'd', '9', '1', '2', '3', '4', ',', 'm', 'x', '.', '.'])
       
       
    def test_typeerror(self):
        self.assertRaises(TypeError, list, chain.from_iterable([2, 3]))   

if __name__ == '__main__':
    unittest.main()