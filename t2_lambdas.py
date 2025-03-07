"""This file contains 4 small lambda functions.

lambda_1 
lambda_2
lambda_3
lambda_4

Each function returns another lambda function which takes a list
and modifies it accordingly.
"""

# 1: Given a sentence the lambda function accepts a list with the words
# of the sentence and returns multiple lists containing the word,
# the word uppercase, the word lowercase, the length of the word

SENTENCE_1 = 'This is a lAmBdA FuNction task'
sentence_1_split = SENTENCE_1.split()

def lambda_1():
    """Returns a lambda function, which accepts a list and returns a
    2d list
    """
    return lambda sen: [[sen[word],
                         sen[word].upper(),
                         sen[word].lower(),
                         len(sen[word])]
                         for word in range(len(sen))]

# 2: Given is a sentence and it is spliltted into a list.
# Three functions are created which return lambda functions
# for converting a string in uppercase, lowercase and
# calculating the length. Using map the functions are applied
# to the sentence

SENTENCE_2 = 'This is a lAmBdA FuNction task'
sentence_2_split = SENTENCE_2.split()

def up():
    return lambda word: word.upper()

def low():
    return lambda word: word.lower()

def length():
    return lambda word: len(word)

func_list = [up(), low(), length()]

def lambda_2():
    """Returns a lambda function, which accepts a list and returns a
    2d list
    """
    return lambda sen: list(map(lambda word: list(map(lambda f: f(word), func_list)), sen))

# 3: Given are two lists. The lambda function returns a list
# with common values

a = [1, 11, 23, 44, 16]
b = [2, 3, 5, 6, 7, 8, 44, 16]

def lambda_3():
    """Returns a lambda function, which accepts two lists
    and returns a list with the common elements
    """
    return lambda x,y: [element for element in x if element in y]

# 4: Given is a string. The lambda function takes a list and
# returns it sorted by the the last character of each element
# alphabetically

SENTENCE_3 = 'This is a lAmBdA FuNction task'
sentence_3_split = SENTENCE_3.split()

def lambda_4():
    """Returns a lambda function, which sorts a given list
    by the the last character of each word alphabetically
    """
    return lambda sen: sorted(sen, key = lambda word: word[len(word)-1])

def main():
    print("Function lambda_1:"+"\n")
    for word in lambda_1()(sentence_1_split):
        print(word)

    print("\n" + "Function lambda_2:"+"\n")
    for word in lambda_2()(sentence_2_split):
        print(word)

    print("\n" + "Function lambda_3:"+"\n")
    print(lambda_3()(a,b))

    print("\n" + "Function lambda_4:")
    print(lambda_4()(sentence_3_split))

if __name__ == "__main__":
    main()
