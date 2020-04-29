#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        if a < b :
            return a
        else:
            return b
    else:
        if a > b :
            return a
        else:
            return b
#better approch       
def lesser_of_two_evens_1(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
lesser_of_two_evens_1(2,4)


####MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return Fals
def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or (n1+n2) == 20

makes_twenty(20,10)

####ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)

almost_there(90)

####Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
    pie = math.pi
    return (4/3*(pie)*pow(rad,3))

#different approch 
def vo_1(rad):
    return (4/3*3.14*(rad**3))

vol(4)
vo_1(4)

####Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    return (num >= low and num <= high)

#different approch 
def ran_check_1(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')


####Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
def up_low(s):
    lower=[]
    upper=[]
    for char in list(s):
        if char.islower():
            lower.append(char)
        if char.isupper():
            upper.append(char)
    print(f'No. of Upper case characters : {len(upper)}')
    print(f'No. of Lower case characters : {len(lower)}')

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

####Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5] Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    print(list(set(lst)))


####Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4] Expected Output : -24
lst = [1, 2, 3, -4]
from functools import reduce
multi = lambda x,y: x*y
reduce(multi,lst)


####Write a Python function that checks whether a passed in string is palindrome or not.

#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(s):
    s= s.replace(' ','')
    rever = s[::-1]
    print(rever , s)
    return  s == rever


    