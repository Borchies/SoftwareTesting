import code_anwar
import unittest


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




if __name__ == '__main__':
    unittest.main()
