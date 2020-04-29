####Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"

import string
str2 = "The quick brown fox jumps over the lazy dog"
alphabet=string.ascii_lowercase
def ispangram(str1, alphabet=string.ascii_lowercase):
    str1_set = set(str1.lower())
    alphabet_set = set(alphabet)
    print(str1_set)
    print(alphabet_set)
    return alphabet_set.issubset(str1_set)

ispangram(str2)