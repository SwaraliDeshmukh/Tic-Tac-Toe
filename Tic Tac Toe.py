def ttt():
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print()
    print("TIC TAC TOE".center(100))
    print("-------------".center(99))
    print()
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print()
    print("Let's Start the Game 🎉!!!!!!")
    print()
    # Grid for playing
    mark=[" "," "," ",
          " "," "," ",
          " "," "," "]
    # Guidelines
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````````")
    print()
    print("1. Player 1 is always 'X' .")
    print()
    print("2. Player 2 is always 'O' .")
    rule="3. Don't Cheat as this is can be played by using only one device."
    print()
    print(rule.upper())
    print()
    print("4. Positions in the grid")
    print("NOTE: Choose only the giver number for the specified location")
    print()
    print("",0," | ",1," | ",2)
    print("---------------")
    print("",3," | ",4," | ",5)
    print("---------------")
    print("",6," | ",7," | ",8)
    print()
    print("```````````````````````````````````````````````````````````````````````````````````````````````````````````````````")

    x=len(mark)
    counter=0
    count=0

    # Winning possibility checker
    def winning_position():
        # For Player 1
        # Rows
        if mark[0]==mark[1]==mark[2]=="X":
            print("Player 1 win's the Game!!!!!")
            return 1
        if mark[3]==mark[4]==mark[5] and mark[3]=="X":
            print("Player 1 win's the Game!!!!!")
            return 1
        if mark[6]==mark[7]==mark[8] and mark[6]=="X":
            print("Player 1 win's the Game!!!!!")
            return 1
        # Columns
        if mark[0]==mark[3]==mark[6] and mark[0]=="X" :
            print("Player 1 win's the Game!!!!!")
            return 1
        if mark[1]==mark[4]==mark[7] and mark[1]=="X" :
            print("Player 1 win's the Game!!!!!")
            return 1
        if mark[2]==mark[5]==mark[8] and mark[2]=="X" :
            print("Player 1 win's the Game!!!!!")
            return 1
        # Diagonals
        if mark[0]==mark[4]==mark[8] and mark[0]=="X" :
            print("Player 1 win's the Game!!!!!")
            return 1
        if mark[0]==mark[6]==mark[8] and mark[0]=="X":
            print("Player 1 win's the Game!!!!!")
            return 1

        # For Player 2
        # Rows
        if mark[0]==mark[1]==mark[2]=="O":
            print("Player 2 win's the Game!!!!!")
            return 1
        if mark[3]==mark[4]==mark[5] and mark[3]=="O":
            print("Player 2 win's the Game!!!!!")
            return 1
        if mark[6]==mark[7]==mark[8] and mark[6]=="O":
            print("Player 2 win's the Game!!!!!")
            return 1
        # Columns
        if mark[0]==mark[3]==mark[6] and mark[0]=="O" :
            print("Player 2 win's the Game!!!!!")
            return 1
        if mark[1]==mark[4]==mark[7] and mark[1]=="O" :
            print("Player 2 win's the Game!!!!!")
            return 1
        if mark[2]==mark[5]==mark[8] and mark[2]=="O" :
            print("Player 2 win's the Game!!!!!")
            return 1
        # Diagonals
        if mark[0]==mark[4]==mark[8] and mark[0]=="O" :
            print("Player 2 win's the Game!!!!!")
            return 1
        if mark[0]==mark[6]==mark[8] and mark[0]=="O":
            print("Player 2 win's the Game!!!!!")
            return 1
        return 0

    # Start The main game   
    def ticTacToe():
        # Grid for positon
        grid_=grid()

        # Taking name 
        name1=input("Enter name of Player1 : ")
        print()
        name2=input("Enter name of Player2 : ")
        print()
        player=1
        x=len(mark)
        counter=0
        count=0

        #location_=location(player,comp)
        while True:
            print(mark[0] +" | "+mark[1]+" | "+mark[2])
            print("---------")
            print(mark[3] +" | "+mark[4]+" | "+mark[5])
            print("---------")
            print(mark[6] +" | "+mark[7]+" | "+mark[8])
            print()

            # Calling the function to check if we got the winner or not
            count=winning_position()

            # Looping for players to play their turns 
            if counter==9 or count==1:
                break
            while True:
                if player== 1:
                    player_1=int(input("{}'s turn : ".format(name1)))
                    if player_1 in range(x) and mark[player_1] == " ":
                        mark[player_1]="X"
                        player=2
                        break
                    else:
                        print("Invalid loaction")
                        print("Play again")
                        continue
                else:
                    player_2=int(input("{}'s turn : ".format(name2)))
                    if player_2 in range(x) and mark[player_2] == " ":
                        mark[player_2]="O"
                        player=1
                        break
                    else:
                        print("Invalid loaction")
                        print("Play again")
                        continue
            counter+=1

    count_=winning_position()

    for i in range(9):
        if mark[i]!=" " and not count_ :
                print("Yay")


    # Displays the grid for playing
    def grid():
        print(mark[0] +" | "+mark[1]+" | "+mark[2])
        print("---------")
        print(mark[3] +" | "+mark[4]+" | "+mark[5])
        print("---------")
        print(mark[6] +" | "+mark[7]+" | "+mark[8])
        print()



    var=ticTacToe()      
    
ttt()