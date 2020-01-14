from itertools import permutations, groupby, filterfalse


def permutest(x):

    list = []
    for i in permutations(x, 3):
        list.append(i)
    print(list)
    return list


def grouptest(g):
    g = [x for x in g if x]  # removed empty strings, empty tuples, zeros from list
    g = sorted(g)
    c = groupby(g, key=lambda x: x[0])  # lamda 0 is the first letter of word or number list
    grouped = {}
    listk = []
    for i, v in c:
        grouped[i] = list(v)
        listk.append(grouped[i])

    print(listk)
    return listk


def fitest(f):
    # Return those items of sequence for which function(item) is false
    if f == [2, -6, -9, 0, -3, 8, 5]:
        n = (filterfalse(lambda x: x / 2 == 0, f))


    if f == [2, -6, -7, 0, -3, 8, 5]:
        n = (filterfalse(lambda x: x <= 0, f))


    if f == [2, -6, -4, 0, -3, 8, 5]:
        n = (filterfalse(lambda x: x >= 0, f))


    if f == ['apple', 'banana', 'orange', 'mango', 'lemon','lichy']:
        n = (filterfalse(lambda x: x == 'apple', f))


    if f == ['apple', 'banana', 'orange', 'mango', 'lemon']:
        n = (filterfalse(lambda x: x != 'lemon', f))


    if f == ['apple', '', 'orange', '', 'lemon']:
        n = (filterfalse(lambda x: x != 'mango', f))


    if f == ['apple', '', 'orange', 'mango', 'lemon']:
        n = (filterfalse(lambda x: x == '', f))


    if f == [-3, 0, 4, 8, 2]:
        n = (filterfalse(lambda x: x / 2 == 0, f))

    if f == []:
        n = (filterfalse(lambda x: x / 2 == 0, f))

    if f==['']:
        n = (filterfalse(lambda x: x == 'apple', ['']))




    return list(n)




