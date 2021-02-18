#This code only for count letters
"""
n = input("Please enter a string\n")

def most_frequent(n):
    dict = {}
    for i in n:
        keys = dict.keys()
        if i in keys:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict

print(most_frequent(n))
"""

#Here final code
>>> from collections import Counter
>>> Counter('mississippi').most_common()

#Output - [('i', 4), ('s', 4), ('p', 2), ('m', 1)]
