print("________Tic Tac Toe Game________")
name_1 = input("Enter the player_1 name:")
name_2 = input("Enter the player_2 name:")
print("________Tic Tac Toe Board________")
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Game_is_still_going = True
winner = None
flag = 0
count = 0
count1 = 0

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2] + "\t\t\t" + str(1) + " | " + str(2) + " | " + str(3))
    print(board[3] + " | " + board[4] + " | " + board[5] + "\t\t\t" + str(4) + " | " + str(5) + " | " + str(6))
    print(board[6] + " | " + board[7] + " | " + board[8] + "\t\t\t" + str(7) + " | " + str(8) + " | " + str(9))

displayBoard()

player_1 = input("Enter the choice between X and 0:")
while (player_1 != 'X') and (player_1 != str(0)):
    print("Please enter the valid choice.")
    player_1 = input("Enter the choice between X and 0:")
print("Player_1 select", player_1)
if player_1 == str(0):
    player_2 = 'X'
    print("Player_2 select", player_2)
elif player_1 == 'X':
    player_2 = str(0)
    print("Player_2 select", player_2)

def PlayingGame():
    global winner, name_1, name_2, count, count1, flag
    while Game_is_still_going:
        print("\nPlayer_1 Turn.")
        index = int(input("Enter the index between 1 to 9:"))
        while index >= 10:
            print("Enter the valid index.")
            index = int(input("Enter the index between 1 to 9:"))
        while (board[index - 1] == player_1) or (board[index - 1] == player_2):
            print("This index is already taken.")
            index = int(input("Enter the index between 1 to 9:"))
            while index >= 10:
                print("Enter the valid index.")
                index = int(input("Enter the index between 1 to 9:"))
        board[index - 1] = player_1
        displayBoard()

        if check_rows():
            flag = 1
            winner = check_rows()
            break
        if check_column():
            flag = 1
            winner = check_column()
            break
        if check_diagonal():
            flag = 1
            winner = check_diagonal()
            break
        if check_draw():
            break
            

        print("\nPlayer_2 Turn.")
        index = int(input("Enter the index between 1 to 9:"))
        while index >= 10:
            print("Enter the valid index.")
            index = int(input("Enter the index between 1 to 9:"))
        while (board[index - 1] == player_1) or (board[index - 1] == player_2):
            print("This index is already taken.")
            index = int(input("Enter the index between 1 to 9:"))
            while index >= 10:
                print("Enter the valid index.")
                index = int(input("Enter the index between 1 to 9:"))
        board[index - 1] = player_2
        displayBoard()

        if check_rows():
            flag = 1
            winner = check_rows()
            break
        if check_column():
            flag = 1
            winner = check_column()
            break
        if check_diagonal():
            flag = 1
            winner = check_diagonal()
            break

    if flag == 1:
        print(winner, "Wins The Game.")
    else:
        print(check_draw())
    ScoreBoard()

def check_rows():
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

def check_column():
     column_1 = board[0] == board[3] == board[6] != "-"
     column_2 = board[1] == board[4] == board[7] != "-"
     column_3 = board[2] == board[5] == board[8] != "-"
     if column_1:
        return board[0]
     if column_2:
        return board[1]
     if column_3:
        return board[2]

def check_diagonal():
     diagonal_1 = board[0] == board[4] == board[8] != "-"
     diagonal_2 = board[2] == board[4] == board[6] != "-"
     if diagonal_1:
         return board[0]
     if diagonal_2:
         return board[2]

def check_draw():
    if board[0] != "-":
        if board[1] != "-":
            if board[2] != "-":
                if board[3] != "-":
                    if board[4] != "-":
                        if board[5] != "-":
                            if board[6] != "-":
                                if board[7] != "-":
                                    if board[8] != "-":
                                        return "The Game Is Draw."

def ScoreBoard():
    global winner, count, count1
    print("\n--------ScoreBoard--------")
    print("--------------------------")
    if winner == player_1:
        count = count + 1
        print("\t\t", name_1 + " =", count)
        print("\t\t", name_2 + " =", count1)
    if winner == player_2:
        count1 = count1 + 1
        print("\t\t", name_1 + " =", count)
        print("\t\t", name_2 + " =", count1)
    print("--------------------------")
PlayingGame()
choice = input("Press 'Quit' to exit the game or 'Yse' to continue the game:")
while (choice != 'Quit') and (choice != 'Yes'):
    print("Enter the valid choice.")
    choice = input("Press 'Quit' to exit the game or 'Yse' to continue the game:")
while choice == 'Yes':
    print("\n________Tic Tac Toe Board________")
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    Game_is_still_going = True
    winner = None
    def displayBoard():
        print(board[0] + " | " + board[1] + " | " + board[2] + "\t\t\t" + str(1) + " | " + str(2) + " | " + str(3))
        print(board[3] + " | " + board[4] + " | " + board[5] + "\t\t\t" + str(4) + " | " + str(5) + " | " + str(6))
        print(board[6] + " | " + board[7] + " | " + board[8] + "\t\t\t" + str(7) + " | " + str(8) + " | " + str(9))
    displayBoard()
    PlayingGame()
    choice = input("Press 'Quit' to exit the game or 'Yse' to continue the game:")