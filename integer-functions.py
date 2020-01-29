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