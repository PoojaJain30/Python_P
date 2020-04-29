  
###SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 #spy_game([1,2,4,0,0,7,5]) --> True
 #spy_game([1,0,2,4,0,5,7]) --> True
 #spy_game([1,7,2,0,4,5,0]) --> False   

def spy_game(nums):
    pattren = [0,0,7,'x']
    for n in nums:
        if pattren[0] == n:
            pattren.pop(0)
    return len(pattren) == 1
            
# another approch  
def spy_game1(nums):
    count = 0
    for num in nums:
        if num == 0:
            count += 1           
        elif num == 7 and count >= 2:
            return True    
    return False