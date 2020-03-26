##Your assignment: Create a Tic Tac Toe game. You are free to use any IDE you like.
##Here are the requirements:
#2 players should be able to play the game (both sitting at the same computer)
#The board should be printed out every time a player makes a move
#You should be able to accept input of the player position and then place a symbol on the board

##variables
import random
game_on = True
Board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2 = ''

#Display Board
def display_board(Board):
    print(f'BOARD \n{Board[1]} | {Board[2]} | {Board[3]} \n---------\n{Board[4]} | {Board[5]} | {Board[6]} \n---------\n{Board[7]} | {Board[8]} | {Board[9]}')

#player input 
def player_input():
    global player1
    global player2
    player1 = (input('Type X or O for Player1:')).upper()
    if player1 == 'X':
         player2 = 'O'
    else:
         player2 = 'X'
    print(f'Player1:{player1}')
    print(f'Player2:{player2}')
    

# Choose which on go first
def choose_first():
    number = random.randint(0,9)
    if number%2 == 0 :
        return 'player1'
    else:
        return 'player2'
    
#Check where space is avilable 
def space_check(Board, position):
    return Board[position] == ' '
        
#Get the choice of player  
def player_choice(Board):
    position = int(input('Choose a position from the Board:'))
    while(not space_check(Board, position)):
        print('Position is already filled!!')
        position = int(input('Choose another position from the Board:'))
    return position 

#place marker on the choosen position
def place_marker(Board, mark, position):
    print('place marker')
    Board[position] = mark
    
#full board check 
def full_board_check(Board):
    digitlist = [ x for x in Board if x == ' ' ]
    return len(digitlist) == 0
        
#win check board       
def win_check(Board, mark):
     return (Board[1] == Board[2]== Board[3] == mark) or (Board[4] == Board[5]== Board[6] == mark) or (Board[7] == Board[8]== Board[9] == mark) or (Board[1] == Board[4]== Board[7] == mark) or(Board[2] == Board[5]== Board[8] == mark) or (Board[3] == Board[6]== Board[9] == mark) or (Board[1] == Board[5]== Board[9] == mark) or (Board[3] == Board[5]== Board[7] == mark)

#Want to replay 
def replay():
    re = (input('Type Y if you want to replay the game:')).upper()
    return re == 'Y'

while True:
    print('Welcome to "Tic-Tac-Toe"')
    print('In order to select the position from teh board type any number between 1 to 9')
    player_input()
    display_board(Board)
    if choose_first()== 'player1':
        first_go = True
    else:
        first_go = False
    while game_on:
        if first_go:
            mark = player1
            print(f"{mark}'s turn")
            position = player_choice(Board)
            place_marker(Board, mark, position)
            display_board(Board)
            first_go = False
            if win_check(Board,mark):
                print('Player1 wins')
                break
                
            if full_board_check(Board):
                print('Its a tie')
                break   
        else:
            mark = player2
            print(f"{mark}'s turn")
            position = player_choice(Board)
            place_marker(Board, mark, position)
            display_board(Board)
            first_go = True
            if win_check(Board,mark):
                print('Player2 wins')
                break
                
            if full_board_check(Board):
                print('Its a tie')
                break
                
    if not replay():
        print('Bye Bye')
        break
    else:
        Board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']