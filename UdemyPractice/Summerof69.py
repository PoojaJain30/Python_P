####SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    sum_array = 0
    cond = True
    for c in (arr):
        while cond:
            if c != 6:
                sum_array = sum_array + c
                break
            else :
                cond = False 
        while not cond:
            if c != 9:
                break
            else:
                cond = True 
                break 
    return sum_array
summer_69([1, 3, 5])