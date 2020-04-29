####Problem 1 Use map() to create a function which finds the length of each word in the phrase (broken by spaces) and returns the values in a list.
    #The function will have an input of a string, and output a list of integers.

phrase = 'How long are the words in this phrase'
def word_lengths(phrase):
    y = phrase.split()
    x = map(lambda n:len(n),y)
    print(list(x)) 
    
#another solution 
def word_lengths1(phrase):
    y = phrase.split()
    def length(n):
        return len(n)
    x = map(length,y)
    print(list(x)) 


####Problem 2 Use reduce() to take a list of digits and return the number that they correspond to. For example, [1, 2, 3] corresponds to one-hundred-twenty-three. Do not convert the integers to strings!

from functools import reduce

def digits_to_num(digits):
    return reduce(lambda x,y:x*10+y,digits)
    
digits_to_num([3,4,3,2,1])

####Problem 3 Use filter() to return the words from a list of words which start with a target letter.
def filter_words(word_list, letter):
   return list(filter(lambda words:words[0]==letter,word_list))

words = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(words,'h')


####Problem 4 Use zip() and a list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with a connector between them. Look at the example output below:

def concatenate(L1, L2, connector): 
   return [x1+connector+x2 for (x1,x2) in zip(L1,L2)]

concatenate(['A','B'],['a','b'],'-')


####Problem 5 Use enumerate() and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.

def d_list(L):
    return {key:value for value,key in enumerate(L)}
d_list(['a','b','c'])


####Problem 6 Use enumerate() and other skills from above to return the count of the number of items in the list whose value equals its index.

def count_match_index(L): 
    return len([index for index,item in enumerate(L) if (item == index )])
    
count_match_index([0,2,2,1,5,5,6,10])