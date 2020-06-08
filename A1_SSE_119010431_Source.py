import random
print(" For an 8-number puzzle, it has a square-framed board consisting of 8 square tiles, numbered 1 to 8, initially placed in random order, while a 15-number puzzle there are 15 numbered square tiles, from 1 to 15, as shown above.  The board has an empty space where an adjacent tile can be slid to.  The objective of the game is to re-arrange the tiles into a sequential order by their numbers (left to right, top to bottom) by repeatedly making sliding moves (left, right, up or down).  The following figure shows an example of an 8-number puzzle where “INITIAL” is the starting point of the game, and the player needs to repeatedly slide an adjacent tile, one at a time, to the currently unoccupied space (the empty space) until all numbers appear sequentially, ordered from left to right, top to bottom, shown as “FINAL”")
print("Initial"),print(3,2,1),print(5,6,4),print(' ',9,8)
print("Final"),print(1,2,3), print(4,5,6), print(8,9," ") #show rules to player

def onestep_8(position):  #the movement of one step in 8 blocks game
    if (position==0):#detect the place of blocks
        move=input(print("choose the number you want to move, enter keys for right",d,"down",s))# gain player movement
        if move== s:#judge whether the move is valid
            board[0]=board[3]
            board[3]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[3]=0#move and print result
        elif move== d:
            board[0]=board[1]
            board[1]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[1]=0
        else:
            print("incorrecct input")
    
    if (position==2):#the same as above, in a different block position
        move=input(print("choose the number you want to move, enter keys for left",a,"down",s))
        if move== s:
            board[2]=board[5]
            board[5]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[5]=0
        elif move== a:
            board[2]=board[1]
            board[1]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[1]=0
        else:
            print("incorrecct input")
    
    if (position==6):
        move=input(print("choose the number you want to move, enter keys for right",d,"up",w))
        if move== w:
            board[6]=board[3]
            board[3]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[3]=0
        elif move== d:
            board[6]=board[7]
            board[7]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[7]=0
        else:
            print("incorrecct input")
    
    if (position==8):
        move=input(print("choose the number you want to move, enter keys for right",d,"up",w))
        if move== a:
            board[8]=board[7]
            board[7]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[7]=0
        elif move== w:
            board[8]=board[5]
            board[5]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[5]=0
        else:
            print("incorrecct input")
    
    if (position==1):
        move=input(print("choose the number you want to move, enter keys for 'left'",a,"'right'",d,"'down'",s))
        if move== a:
            board[1]=board[0]
            board[0]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[0]=0
        elif move== d:
            board[1]=board[2]
            board[2]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[2]=0
        elif move==s:
            board[1]=board[4]
            board[4]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])  
            board[4]=0          
        else:
            print("incorrecct input")

    if (position==3):
        move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s))
        if move== w:
            board[3]=board[0]
            board[0]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[0]=0
        elif move== d:
            board[3]=board[4]
            board[4]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[4]=0
        elif move==s:
            board[3]=board[6]
            board[6]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[6]=0
        else:
            print("incorrecct input")

    if (position==5):
        move=input(print("choose the number you want to move, enter keys for 'up'",w,"'left'",a,"'down'",s))
        if move== w:
            board[5]=board[2]
            board[2]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[2]=0
        elif move== a:
            board[5]=board[4]
            board[4]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[4]=0
        elif move==s:
            board[5]=board[8]
            board[8]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[8]=0
        else:
            print("incorrecct input")
    
    if (position==7):
        move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'left'",a))
        if move== w:
            board[7]=board[4]
            board[4]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[4]=0
        elif move== d:
            board[7]=board[8]
            board[8]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[8]=0
        elif move==a:
            board[7]=board[6]
            board[6]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[6]=0
        else:
            print("incorrecct input")

    if (position==4):
        move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s,"'left'",a))
        if move== w:
            board[4]=board[1]
            board[1]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[1]=0
        elif move== d:
            board[4]=board[5]
            board[5]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[5]=0
        elif move==s:
            board[4]=board[7]
            board[7]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[7]=0
        elif move==a:
            board[4]=board[3]
            board[3]=("")
            print(board[:3]),print(board[3:6]),print(board[6:9])
            board[3]=0
        else:
            print("incorrecct input")            

def onestep_15(position):#the on move in 15 blocks games
        judge=1#value for valid test
        if (position==5):#test posotion of the empty blocks
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s,"'left'",a))#gain users input
        if (position==6):#same as above
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s,"'left'",a))
        if (position==9):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s,"'left'",a))
        if (position==10):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s,"'left'",a))
        elif (position==1):#same 
            move=input(print("choose the number you want to move, enter keys for 'right'",d,"'down'",s,"'left'",a))
            if move==d:# judge if input is valid
                judge=1#valid 
            elif move==s:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")#response for not valid input
                judge=0# not valid
        elif (position==2):
            move=input(print("choose the number you want to move, enter keys for 'right'",d,"'down'",s,"'left'",a))
            if move==d:
                judge=1
            elif move==s:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==4):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s))
            if move==d:
                judge=1
            elif move==s:
                judge=1
            elif move==w:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==8):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'down'",s))
            if move==d:
                judge=1
            elif move==s:
                judge=1
            elif move==w:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==7):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'down'",s,"'left'",a))
            if move==w:
                judge=1
            elif move==s:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==11):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'down'",s,"'left'",a))
            if move==w:
                judge=1
            elif move==s:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==13):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'left'",a))
            if move==d:
                judge=1
            elif move==d:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==14):
            move=input(print("choose the number you want to move, enter keys for 'up'",w,"'right'",d,"'left'",a))
            if move==d:
                judge=1
            elif move==w:
                judge=1
            elif move==a:
                judge=1
            else:
                print("invorrect input")
                judge=0
        elif(position==0):
            move=input(print("choose the number you want to move, enter keys for 'right'",d,"'down'",s))
            if move==d:
                judge=1
            elif move==s:
                judge=1
            else:
                print("incorrect input")
                judge=0
        elif(position==3):
            move=input(print("choose the number you want to move, enter keys for'down'",s,"'left'",a))
            if move==a:
                judge=1
            elif move==s:
                judge=1
            else:
                print("incorrect input")
                judge=0
        elif(position==12):
            move=input(print("choose the number you want to move, enter keys for'up'",w,"'right'",d))
            if move==d:
                judge=1
            elif move==w:
                judge=1
            else:
                print("incorrect input")
                judge=0
        elif(position==15):
            move=input(print("choose the number you want to move, enter keys for'up'",w,"'left'",a))
            if move==w:
                judge=1
            elif move==a:
                judge=1
            else:
                print("incorrect input")
                judge=0
        
        if (move==w):#move for up
            if(judge==1):
                board[position]=board[(position-4)]
                board[(position-4)]=("")
                print(board[:4]),print(board[4:8]),print(board[8:12]),print(board[12:16])
                board[(position-4)]=0
        elif (move==s):#move for down
            if judge==1:
                board[position]=board[(position+4)]
                board[(position+4)]=("")
                print(board[:4]),print(board[4:8]),print(board[8:12]),print(board[12:16])
                board[(position+4)]=0
        elif (move==a):#move for left
            if judge==1:
                board[position]=board[(position-1)]
                board[(position-1)]=("")
                print(board[:4]),print(board[4:8]),print(board[8:12]),print(board[12:16])
                board[(position-1)]=0
        elif (move==d):#move for right
            if judge==1:
                board[position]=board[(position+1)]
                board[(position+1)]=("")
                print(board[:4]),print(board[4:8]),print(board[8:12]),print(board[12:16])
                board[(position+1)]=0#show move result

statu_check=1  #valid test
test=1#valid test
def startgame8():#function of the main game of 8 blocks
    global test
    global statu_check
    random.shuffle(board)#make a random list
    t=(board.index(0))
    board[(board.index(0))]=("")
    print(board[:3]),print(board[3:6]),print(board[6:9])#show players the initial status
    board[t]=0
    step_count=0#for counting how many steps that player uses
    while statu_check==1:
        if board==[1,2,3,4,5,6,7,8,0]:#win situation
            print("Congratulation! You solve the puzzle! You use",step_count,"steps in total")
            game_end=input(print("if you want to restart, press'r',if you want to quit, press'q'"))
            if game_end==("r"):#for restart the game
                statu_check=0
                test=1#reset value check
            else:
                print("game will now quit")#quit the game
                statu_check=0
                exit()
        else:
            onestep_8(board.index(0))#game move on
            step_count+=1#count each step
            continue

def startgame15():#for 15 blocks game, every steps is same as 8 blocks
    global test
    global statu_check
    random.shuffle(board)
    t=(board.index(0))
    board[(board.index(0))]=("")
    print(board[:4]),print(board[4:8]),print(board[8:12]),print(board[12:16])
    board[t]=0
    step_count=0
    while statu_check==1:
        if board==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
            print("Congratulation! You solve the puzzle! You use",step_count,"steps in total")
            game_end=input(print("if you want to restart, press'r',if you want to quit, press'q'"))
            if game_end==("r"):
                statu_check=0
                test=1
            else:
                print("game will now quit")
                test=0
                statu_check=0
                exit()
        else:
            onestep_15(board.index(0))
            step_count+=1
            continue

while test==1:#the main game programme
    (w,s,a,d)=input("please enter 4 keys for up, down, left and right movement")#gain players settings
    gametype=int(input("enter '8'for 8number game,'15'for 15number game"))#choose game type
    if gametype==8:#load 8 blocks game
        board=[1,2,3,4,5,6,7,8,0]
        startgame8()
    elif gametype==15:# load 15 blocks game
        board=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
        startgame15()
    else:
        print("please enter 8 or 15 for game type")#for wrong input
        test=1



