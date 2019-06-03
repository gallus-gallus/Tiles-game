############## DEFINE FUNCTIONS AND VARIABLES ##############
board=[]
points=0
points_ratio=""
moves=0
string=''
mode=1
import random
pieces=[["A",'O','B','Y','M','E','Z','X','I'],["©",'§','√','+','ø',"∫"]] #List of charaters in game. Item one is the basic characters. Item two is special characters.
#1=coin(100 points) 2=Win if break 3=Unbreakable wall 4=conector (ships momentum) 5=Bomb 6=breakable wall
Alphabete=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
help=Alphabete.copy() #copy the list alphabete into help
for i in Alphabete:
    help.append(i.lower()) #so t intem i in alphabete, turned into lower case
Alphabete=[] #empty
Alphabete=help #remplace it with lower case an caps
#print(Alphabete)
#alphabete
def instructions(): #will return instructions
    return '''Hi, welcome to this tile game'''
def is_alphabetical(string): # will return true if all characters are in the alphabet, lower and caps. Else it returns false
    global Alphabete #import alphabete
    string2='' #clear variables
    string2=str(string)#this way we can change the variable
    alph=True #preset to true
    analize=[] #clear
    an=0 #clear
    this_list=[] #clear
    for i in string2: #make a list out of string2
        this_list.append(i) #append letter i to list
    for i in this_list: #for i in the list
        for j in Alphabete: #so for every letter of the alphabet, caps and not
            if i==j: # if i is in the alphabet
                analize.append(True) #we now know that a letter was in the alphabet
                an=1 #we confirm that in this iteration there was a valid letter
                break #break loop of alphabet
        if an==0: #if the character is not a letter
            analize.append(False) #add false to list
        an=0 #reset analize
    for i in analize: #our false/true list
        if i==False:
            alph=False #there is a character that is not alphabetical
    return alph #alph was preset to true, so it is only if the if gave a false that it will be false

class Board: #THIS WILL DO ANYTHING THAT HAS TO DO WITH THE BOARD
    def __init__(self,Xsize,Ysize,help_list,help_var): #define self
        self.Xsize=Xsize
        self.Ysize=Ysize
        self.help_list=help_list
        self.help_var=help_var
    def drop_peices(self,x,y,list):
        #this function will take a certain spot in a list (list) and delete a point(x,y), then drop everything abouve it into the point.
        hold_list = [] #Reset stuff
        finish_list=[] #^
        finish_list=list #This way we can change the value of finish_list, unlike list
        hold_list.append(random.choice(pieces[0])) #This will be the top piece, that will need to be random
        for i in range(0,y+1,1): #Repeat until you hit y+1 position (+1 so it goes to y)
            hold_list.append(finish_list[i][x]) #append the letter that was in the spots abouve x,y
        del hold_list[len(hold_list)-1] #Delete the letter that was at x,y
        #if len(hold_list)==y: (test)
        for i in range(0,y+1,1): #Repeat until you hit y+1 position (+1 so it goes to y)
            finish_list[i][x]=hold_list[i] #remplace x, <=y with the "dropped list"
        return finish_list #return the updated list

    def create_board(self): #MAKES RANDOM BOARD
        global mode
        global pieces
        global board #bad habits on my part
        self.help_list=[] #reset
        if mode==1: #so, if we want a random board
            for i in range(0,self.Ysize,1): #in y size
                for j in range(0,self.Xsize,1): #in xsize
                    self.help_list.append(random.choice(pieces[0]))#Add a RANDOM IMPORTANT TO CHANGE TO MORE THINGS
                board.append(self.help_list) #Add the random stuff to the board
                #test: print(help_list)
                self.help_list=[] #reset
    def print_board(self): #PRINTS BOARD
        for i in range(1,20,1): # add distance with last board here
            print()
        global board
        global Alphabete
        self.help_list=[]
        self.help_var=""
        #empty these to keep things clean
        helpvar2=0
        #this too
        self.help_list=Alphabete
        #now self.help_list is equal to the alphabet
        self.help_var+="  |"
        #this is the first character on the board, so we add it first
        for i in self.help_list: #HERE WE WILL ADD THE X DIRETION KEY
            for j in i:
                self.help_var+=j #add the letter
            self.help_var+="|" #add this again
            helpvar2+=1 #keep track of the number of iterations of the loop
            if helpvar2==self.Xsize: #break loop if the nuber of iterations is equal to the x size of the board
                break
        print(self.help_var) #print all that
        print(" ","-"*(helpvar2*2+1)) #print separation line
        helpvar2=0 #reset
        #HERE WE PRINT THE BOARD
        for i in board: #ie for y size of board
            helpvar2+=1 #track the iterations of the loop
            if helpvar2<10: #if this is not here, as soon as you get to ten, the board is scewed over
                self.help_var=str(helpvar2)+" " #so we add a space on low  nubers to compensate
            else:
                self.help_var=str(helpvar2) # else we just print the number!
            self.help_list=[] # reset list (in loop)
            self.help_list.append("|") # add first separator
            for j in i: # for the x size of board
                self.help_list.append(j) # append letter (remeber we already added first separator)
                self.help_list.append("|") #add separators
            for j in self.help_list: # This way we remouve the [''] around the letter
                self.help_var+=j
            print(self.help_var) # and PRINT
    def switch_pieces(self,x,y,direction,list):  # will switch peice x, y
        board=list  #To use as list
        store_pos_1=0  # Reset
        store_pos_2=0  # Reset
        edit_list=list  # We will edit this list to create the new board
        if direction == "h":  # If direction is Horizantal
            store_pos_1=list[y][x]  #Store pos x, y
            store_pos_2=list[y][(-1*x)-1]  # Remember that a negative valued object of the list is the same as (-1*value)-1 item of the list. Here we want to be on the other end of the list, so we are using  negative values.
            edit_list[y][x]=store_pos_2  #remplace first position with value form second position
            edit_list[y][(-1*x)-1]=store_pos_1  #Remplace second position with value from first position
            return edit_list  # return the edited list
        if direction == "v":  #If direction is vertical
            store_pos_1=list[y][x]  #store position x, y
            store_pos_2=list[(-1*y)-1][x]  # Remember that a negative valued object of the list is the same as (-1*value)-1 item of the list. Here we want to be on the other end of the list, so we are using  negative values.
            edit_list[y][x]=store_pos_2  #remplace first position with second value
            edit_list[(-1*y)-1][x]=store_pos_1 #remplace second position with first value
            return edit_list  # return edited list




This_board = Board(10, 10, [], "")

class Move: #deals with moves
    def __init__(self,move): #when initialized
        self.move=move #add move list
    def ask_move_row(self): #will ask for input and return with message :Please enter your row (number)."
        return input("Please enter your row (number).") #return
    def row_valid(self,item_inputed): #verifies that the row inputed is valid, and askes for row.
        move_append=0 #reset
        try: #assumes that inputed value is integer
            if int(item_inputed) <= This_board.Ysize and int(item_inputed)>0: #if inputed value is within range
                print("Ok!") #print ok
                move_append=item_inputed #add here so that it can be used later
            else: #if out of range
                print("Looks like your input was out of range!") #notify
                move_inputed2=Move.ask_move_row(self) #ask for move again
                while int(move_inputed2) > This_board.Ysize or int(move_inputed2)<=0: #repeat untill within range
                    print("Looks like your input was out of range!") #notify again
                    move_inputed2=Move.ask_move_row(self) #ask for move again
                print("Ok, your good!") #notify that all is well
                move_append=move_inputed2 #add value here to use later
        except ValueError: #if value inputed is not number
            print("Looks like that is not a number! Try again.") #notify
            Move.row_valid(self,Move.ask_move_row(self)) #recall function
        if move_append!=0: #makes shure this is not a useless recall
            self.move.append(int(move_append)-1) #add to use later (-1 to stay compatible with lists)
        return True #return that all is well


    def ask_move_column(self): #will ask for input and check to see if input is valid. Will restart if necessary
        '''Please note that this function calls itself if there is a bad input. This might be your problem.'''
        global Alphabete  #we will need this later. it contains caps and lower of the whole alphabet
        my_answer_letter=input("Please enter your column (letter).")  #get info
        if my_answer_letter.isalpha() and len(my_answer_letter)==1:  #is the input basicly good (letter, and only one letter?)
            my_answer_letter=my_answer_letter.upper()  #Make sure that the answer is UPPER CASE
            alphabete1_26=Alphabete[0:26] #Get only the caps from the alphabet and put it in another list (alphabete1_26)
            iterations=0  #reset this
            my_digit_answer=0  #This variable will be our final answer
            for i in alphabete1_26: #ITTERATE through an UPPER case alphabet
                iterations+=1  #change iterations by one to keep track
                if i==my_answer_letter:  #If the input and the i match, we know we have found the right answer.
                    my_digit_answer=iterations  #Save the number of iterations requiered to get here as our answer.
            if my_digit_answer > 0 and my_digit_answer <= This_board.Ysize:  #Make sure the board size matches
                #print(my_digit_answer)  # good test!
                self.move.append(my_digit_answer-1) #add the answer -one (to be compatible with lists) to our move portfolio
                print("Ok. Good to go!")  #notify that all is good.
                return my_digit_answer #return answer just in case
            else: #if the letter is outside the board
                print("Looks like you picked a column that was out of range. Please try again. :)") #notify! :)
                Move.ask_move_column(self)  #And start over again.
        else:  #if something whecky is going on
            print("Woops. Lets try that again.") #notify
            #while not my_answer_letter.isalpha() and len(my_answer_letter)!=1:
            #    my_answer_letter=input("Please enter your column (letter) as one single letter corresponding to a column.")
            This_move.ask_move_column()  #start over
    def direction_of_move(self):  #will ask for direction player wants to move in, U, D, L, R.
        direction=input("In which direction would you like to move? U, D, L, or R?") #ask for input
        direction=direction.lower()  #make sure all is in lower case.
        if direction=="u" or direction=="d" or direction=="l" or direction=="r": #see if answer is one of 4 valid inputs
            print("Ok, you are good to go!") #Notify that all si well :)
            This_move.move.append(direction)  #Add to move list for future referance
            return direction  #return just in case
        else:  #Not one of the valid inputs
            print("Please try that again. You can only input U or D or L or R.")  #Ask them to try again
            This_move.direction_of_move() #Restart
    def move_type(self):  #Asks what kind of move player wants to make
        type=input('''What kind of move would you like to make?
M = Menu
S = Switch
D = Delete 3 in a row (with the possibility of activating something)
R = Reset level
N = Skip level (next)(if in random mode, = Regenerate)

''')  #Get input
        type=type.lower()  #Make sure all is lower case
        if type=="m" or type=="s" or type=="d" or type=="r" or type=="n":  #Makes shure that input is one of 5 acceptable inputs
            print("Ok, good to go!")  #notify
            This_move.move.append(type)  #append to list of moves
            return type  #Return just in case
        else:  #if fishy
            print('''Please try again.''')  #notify
            This_move.move_type()  #recall

This_move=Move([])  #create class instance


def one_move():
    global board
    global moves
    global points
    global points_ratio
    bad_move=0
    good_indicator=0
    This_move.move_type()
    if This_move.move[0]=="s" or This_move.move[0]=="d":
        This_move.row_valid(This_move.ask_move_row())
        This_move.ask_move_column()
        This_move.direction_of_move()
        if This_move.move[0]=="s":
            if This_move.move[3]=="l" or This_move.move[3]=="r":
                board=This_board.switch_pieces(This_move.move[2],This_move.move[1],"h",board)
            else:
                board=This_board.switch_pieces(This_move.move[2], This_move.move[1], "v", board)
            This_board.print_board()
        elif This_move.move[0]=="d":
            if This_move.move[2]>=This_board.Xsize-2 and This_move.move[3]=="r":
                bad_move=1
            if This_move.move[2]<=2 and This_move.move[3]=="l":  #if This_move.move[2]<=This_board.Xsize+2 and This_move.move[3]=="l":
                bad_move=1
            if This_move.move[1]>=This_board.Ysize-2 and This_move.move[3]=="d":
                bad_move=1
            if This_move.move[1]<=2 and This_move.move[3]=="u":  #if This_move.move[1]<=This_board.Ysize+2 and This_move.move[3]=="u":
                bad_move=1

            if This_move.move[3] == "r":
                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2] + 1]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2] + 2]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

            if This_move.move[3] == "l":
                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]-1]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]-2]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

            if This_move.move[3] == "u":
                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]-1][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]-2][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

            if This_move.move[3] == "d":
                for i in pieces[0]:
                    if i == board[This_move.move[1]][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]+1][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0

                for i in pieces[0]:
                    if i == board[This_move.move[1]+2][This_move.move[2]]:
                        good_indicator = 1
                if good_indicator == 0:
                    bad_move = 1
                good_indicator = 0


            if This_move.move[3]=="r":
                if board[This_move.move[1]][This_move.move[2]]==board[This_move.move[1]][This_move.move[2]+1] and board[This_move.move[1]][This_move.move[2]+1]==board[This_move.move[1]][This_move.move[2]+2]:
                    pass
                else:
                    bad_move=1
            if This_move.move[3]=="l":
                if board[This_move.move[1]][This_move.move[2]]==board[This_move.move[1]][This_move.move[2]-1] and board[This_move.move[1]][This_move.move[2]-1]==board[This_move.move[1]][This_move.move[2]-2]:
                    pass
                else:
                    bad_move=1
            if This_move.move[3]=="u":
                if board[This_move.move[1]][This_move.move[2]]==board[This_move.move[1]-1][This_move.move[2]] and board[This_move.move[1]-1][This_move.move[2]]==board[This_move.move[1]-2][This_move.move[2]]:
                    pass
                else:
                    bad_move=1
            if This_move.move[3]=="d":
                if board[This_move.move[1]][This_move.move[2]]==board[This_move.move[1]+1][This_move.move[2]] and board[This_move.move[1]+1][This_move.move[2]]==board[This_move.move[1]+2][This_move.move[2]]:
                    pass
                else:
                    bad_move=1

            if bad_move==0:
                if This_move.move[3]=="r":
                    board=This_board.drop_peices(This_move.move[2],This_move.move[1],board)
                    board=This_board.drop_peices(This_move.move[2]+1, This_move.move[1], board)
                    board=This_board.drop_peices(This_move.move[2]+2, This_move.move[1], board)
                if This_move.move[3]=="l":
                    board=This_board.drop_peices(This_move.move[2],This_move.move[1],board)
                    board=This_board.drop_peices(This_move.move[2]-1, This_move.move[1], board)
                    board=This_board.drop_peices(This_move.move[2]-2, This_move.move[1], board)
                if This_move.move[3]=="u":
                    board = This_board.drop_peices(This_move.move[2], This_move.move[1] - 2, board)
                    board = This_board.drop_peices(This_move.move[2], This_move.move[1] - 1, board)
                    board=This_board.drop_peices(This_move.move[2], This_move.move[1],board)
                if This_move.move[3]=="d":
                    board=This_board.drop_peices(This_move.move[2], This_move.move[1],board)
                    board=This_board.drop_peices(This_move.move[2], This_move.move[1]+1, board)
                    board=This_board.drop_peices(This_move.move[2], This_move.move[1]+2, board)
                    #board = This_board.drop_peices(This_move.move[2], This_move.move[1] + 2, board)
                    #board = This_board.drop_peices(This_move.move[2], This_move.move[1] + 1, board)
                    #board = This_board.drop_peices(This_move.move[2], This_move.move[1], board)
                This_board.print_board()
                points+=1
            else:
                print('''
                Invalid move!
                ''')
            bad_move=0
    This_move.move=[]
    moves+=1
    points_ratio=str(points)+"/"+str(moves)
    print('''
You have scored
'''+points_ratio+''' skill rating and you have '''+str(points)+" points.")



# test:This_board.create_board()
#test:print(board)

################ MAIN CODE ################


This_board.create_board()
This_board.print_board()
#board=This_board.drop_peices(4,5,board)
#This_board.print_board()
#print(This_move.move)
#print(This_move.move)  #good test
#board=This_board.switch_pieces(9,9,"v",board)
#This_board.print_board()
while True:
    one_move()