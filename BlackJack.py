####BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST


def blackjack(a,b,c):
    summ = a+b+c
    if(summ > 21 ):
        if((a == 11) or (b == 11) or (c == 11)):
            summ = summ - 10
            if summ < 21:
                return summ
            else:
                return"BUST"
        else:
            return"BUST"
    else:
        return summ
    
#Better approch 

def blackjack_1(a,b,c):
    
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
        
blackjack(5,6,7)
blackjack_1(5,6,7)