####COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number count_primes(100) --> 25

def count_primes(num):
    count = 0
    def check_prime(numb):
        if numb <= 1:
            return False
        for i in range(2,numb):
            if numb%i == 0:
                return False 
        return True

    for n in range(2,num+1):
        if check_prime(n):
            #print(check_prime(n))
            #print(n)
            count += 1

    print(f"The number of prime numbers till {num} is {count}")

#another approch 
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print("hi")
in_num = int(input("Tell me a number and I will give the count of prime numbers for that number"))
count_primes(in_num)

   
    