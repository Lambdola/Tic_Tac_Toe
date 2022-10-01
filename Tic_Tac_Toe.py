#For visual/display interaction only 
print("""
                       TEMPLATE POSITIONS
 User1 = X
 User2 = 0                     
                           a | b | c
                           -- --- --
                           d | e | f
                           -- --- --
                           g | h | i
""")


#Constant variables initialization
N = 19
SPACES = " " * (N)
EXTRA = " " * (N + 1)
SEPARATION = "----  -----  ----"
OP1, OP2 = ("  X ", "  O ")

#Determinant variables initialization 
a = b = c = d = e = f = g = h = i = "    "
GAME_BOARD = [a, b, c, d, e, f, g, h, i]
GB = GAME_BOARD 
KEY = True

#Rows, Columns and Diagonals 
row1 = list(range(0,3))
row2 = list(range(3,6))
row3 = list(range(6,9))
col1 = list(range(0,7,3))
col2 = list(range(1,8,3))
col3 = list(range(2,9,3))
f_diag = list(range(2,7,2))
b_diag = list(range(0,9,4))

#Print out updated Tic_Tac_Toe table 
def check():
    print(f"{SPACES}{GB[0]} | {GB[1]} | {GB[2]}\n{EXTRA}{SEPARATION}\n{SPACES}{GB[3]} | {GB[4]} | {GB[5]}\n{EXTRA}{SEPARATION}\n{SPACES}{GB[6]} | {GB[7]} | {GB[8]}")

 
#Main Game Loop
while KEY:
    i = 0
    j = 0
    id = ["User1", "User2"]
    r, s = id
    while KEY:
        #Repeatedly ask for input position for game options( X or O) 
        while True:
            turn = id[0]
            play = input(f"{turn}: ").lower()
            match = ["a","b","c","d","e","f","g","h","i"]
            if play in match:
                value = match.index(play)
            else:
                value = -1
                
            if value != -1:
                if id[0] == r:
                    GB[value] = OP1
                else:
                    GB[value] = OP2
            else:
              print("Invalid Input")
              continue
            i += 1
            check()
   
            #If X wins 
            if all((GB[i] == OP1 for i in row1)) or all((GB[i] == OP1 for i in row2)) or all((GB[i] == OP1 for i in row3)) or all((GB[i] == OP1 for i in col1)) or all((GB[i] == OP1 for i in col2)) or all((GB[i] == OP1 for i in col3)) or all((GB[i] == OP1 for i in f_diag)) or all((GB[i] == OP1 for i in b_diag)):
                print(f"\"{r}\" win")
                KEY = False
                break

            #If O wins     
            if all((GB[i] == OP2 for i in row1)) or all((GB[i] == OP2 for i in row2)) or all((GB[i] == OP2 for i in row3)) or all((GB[i] == OP2 for i in col1)) or all((GB[i] == OP2 for i in col2)) or all((GB[i] == OP2 for i in col3)) or all((GB[i] == OP2 for i in f_diag)) or all((GB[i] == OP2 for i in b_diag)):
                print(f"\"{s}\" win")
                KEY = False
                break

            #Alternating user display name   
            id[1], id[0] = id[0], id[1]

            #If out of positions 
            if (i == 9):
                KEY = False
                break
            
            

    
  
    
    
        
