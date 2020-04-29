####Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    li = False
    for ints in enumerate(nums):
        if ints == 3 and nums[-2] == 3:
            li = True
        else:
            pass
    return li

#better approch 
def has_33_1(nums):
    for i in range(0,len(nums)-1):
        return nums[i] == 3 and nums[i+1] == 3
            
        
has_33_1([3, 3, 1,3])
has_33([1, 3, 3])