import random
ran_no = random.randint(1,100)
guess_li = [0]
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
while True :
    in_no = int(input("I'm thinking of a number between 1 and 100.\n What number you are thinking :"))
    if (in_no < 1 or in_no > 100) :
        print("OUT OF BOUNDS","Please try another number")
        continue
    
    if (in_no == ran_no) :
        print(f"Congratulations! You have guessed correct number in {len(guess_li)} guesses")
        break
    
    guess_li.append(in_no)

    if (len(guess_li) == 1) :
        if (abs(in_no - ran_no) <= 10) :
            print("WARM!")
        else :
            print("COLD!")
    else :
        if (abs(in_no - ran_no) > abs(guess_li[-2] - ran_no)):
             print("COLDER!")
        else :
            print("WARMER!")

   
        
