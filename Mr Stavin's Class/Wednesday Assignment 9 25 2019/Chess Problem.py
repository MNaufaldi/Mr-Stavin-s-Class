#Problem 1: Chess
# Make a board
CBoard = {}
CBoard_Print = []
move = ""
form = []
def board(howbig):
    #User will input the length or width of the board they want
    #how big will be an int
    #65 - 90 is A - Z | 48 - 57 is 0 - 9
    #Tip create a list for both letter and number in position
    global CBoard 
    global CBoard_Print
    global move
    global form
    CBoard = {}
    CBoard_Print = []
    move = ""
    form = []#These 4 are for reset purposes
    positionLetter = ""
    positionNumber = ""
    for e in range(int(howbig)):
        for el in range(int(howbig)):
            positionLetter=(str(chr(65 + int(el))))
            positionNumber=(str(int(e)+1))
            position = positionLetter + positionNumber
            CBoard[position] = "-"
    Start()
            
#Needed to display the "-" by width x length 
#Needed to 'remake the list' everytime move happened (NOT EFFICIENT) maybe
def printboard():
    global CBoard
    CBoard_Print = [[]] #'tis not the global list
    n = 0
    c = 0
    for keys in CBoard.keys():
        CBoard_Print[n] += CBoard[keys]
        c += 1
        if c == int(howbig):
            CBoard_Print.append([])
            c = 0
            n+=1          
    for n in range(int(howbig)):
        print("  ".join(map(str, CBoard_Print[n])))
    Choices()

#Lets say that user input the position(A1 and stuff) to move the knight
def moveknight():
    global CBoard
    global move
    global form
    RKnight() #Remove the "x" from before
    CBoard[move] = "-"
#The move will be turned to A1 and stuff then
    #im going to put if's to limit the knight movement
    print("Available moves\n",form)
    move = input("Please input your move: ") 
    if move not in form:
        print("Invalid move")
    else:
        CBoard[move] = "o"
        print("Your knight has been moved")
        Knight()
        Choices()
    # o  is the current horse
    
#Knight movement limit
def Knight():
    #Show available move for knight
    #1st and 2nd form (ascii +/- 2 and num +/- 1)
    #NOT EFFICIENT (Maybe) and kinda hard to edit
    global form
    global move
    global CBoard
    form = []
    pmoveL = [-2,-2,-1,-1,+1,+1,+2,+2]
    pmoveN = [-1,+1,-2,+2,-2,+2,-1,+1]
    count = 0
    for notation in list(move):
        if 65 <= ord(notation) <= 90:
            for l in pmoveL:
                form.append(chr(ord(notation)+(l)))
                
        elif 48 <= ord(notation) <= 57:
            for n in pmoveN:
                form[count] += (chr(ord(notation)+(n)))
                count += 1
    for f in range(len(form)-1,-1,-1):
        if form[f] not in CBoard:
            del form[f]
    for f in form:
            CBoard[f] = "x"
        
    
def Start():
    global CBoard
    global move
    move = input("Welcome to chess but only 1 knight\nWhere do you want to put the knight?  ")
    if move not in CBoard:
        print("Invalid Move")
        Start()
    else:
        CBoard[move] = "o"
        print("Your knight has been placed\n")
    Knight()
    Choices()

def Choices():
   global move
   choice = int(input("1. Move Knight\n2. Show Board\n3. Reset\n4. Exit\n\nWhat do you want to do? "))
   if choice == 1:
       moveknight()
   elif choice == 2:
       printboard()
   elif choice == 3:
       board("8")
   else:
       print("Bye")
    
def RKnight():
    global form
    global CBoard
    for el in form:
        CBoard[el] = "-"   
    #To remove the "x" when the knight moved.
howbig = "8" #The limit is 9 because it cant work with 2 digits properly yet and if its too small the move prediciton will mess up
board(howbig)