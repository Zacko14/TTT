def TTTmain():
    print("Welcome to MonTeeTeeTee Python. ")
    # TTTlist = ["-"]*9
    Choiceslist = []
    TTTlist = [['']*3,['']*3,['']*3]
    for i in range(9):
        if i%2 == 0:
            choice = int(input(" It's X player turn. Choice of Location: from upper left (1) to bottom right (9):"))
            while choice in Choiceslist:
                choice = int(input("This square is already taken, Player X. Choose again, cheater:"))
            else:
                # TTTlist[(choice-1)%3][choice-3*(choice-1)%3-1] = "X"
                TTTlist[(choice-1)//3][(choice-1) % 3] = "X"

        if i%2 != 0:
            choice = int(input(" It's 0 player turn. Choice of Location: from upper left (1) to bottom right (9):"))
            while choice in Choiceslist:
                choice = int(input("This square is already taken, Player 0. Choose again, cheater:"))
            else:
                TTTlist[(choice-1)//3][(choice-1) % 3] = "0"
        i += 1
        Choiceslist.append(int(choice))
        print(TTTlist[0])
        print(TTTlist[1])
        print(TTTlist[2])
        if detectwin(TTTlist):
            winnerend(detectwin(TTTlist))
    print("It's a tie.")
    playagain = str(input("Play again? (Y/N)"))
    if playagain == "Y":
        TTTmain()
    else:
        quit()

def detectwin(TTTlist):
    winnerexists = False
    winner = ''
    #check rows
    for i in range(2):
        if TTTlist[i][0] == TTTlist[i][1] and TTTlist[i][0] == TTTlist[i][2] and TTTlist[i][0] != '':
            winnerexists = True
            winner = TTTlist[i][0]
    #check columns
    for i in range(2):
        if TTTlist[0][i] == TTTlist[1][i] and TTTlist[0][i] == TTTlist[2][i]  and TTTlist[0][i] != '':
            winnerexists = True
            winner = TTTlist[0][i]
    #check diagonals
    if TTTlist[0][0] == TTTlist[1][1] and TTTlist[0][0] == TTTlist[2][2]  and TTTlist[0][0] != '':
        winnerexists = True
        winner = TTTlist[0][0]
    if TTTlist[2][0] == TTTlist[1][1] and TTTlist[2][0] == TTTlist[0][2] and TTTlist[2][0] != '':
        winnerexists = True
        winner = TTTlist[2][0]
    return winnerexists, winner

def winnerend(detectwin):
    exists, identity = detectwin
    if exists:
        print(f"Congratulations to Player {str(identity)}. You win!")
        playagain = str(input("Play again? (Y/N)"))
        if playagain == "Y":
            TTTmain()
        else:
            quit()


TTTmain()



