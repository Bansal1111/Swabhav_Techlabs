def board_print(board_list):
    for lists in board_list:
        print(*lists)

def update_board_list(player_input,board_list,player_value):
    row=player_input//3
    column=player_input%3
    if(player_value==1):
        if(column==0):
            board_list[row-1][2]=0
        else:
            board_list[row][column-1]=0
    else:
        if(column==0):
            board_list[row-1][2]='X'
        else:
            board_list[row][column-1]='X'
    board_print(board_list)

def check(board_list):
    #row checking
    if(board_list[0][0]==board_list[0][1]==board_list[0][2] or board_list[1][0]==board_list[1][1]==board_list[1][2] or board_list[2][0]==board_list[2][1]==board_list[2][2]):
        return("win")
    #column checking
    elif(board_list[0][0]==board_list[1][0]==board_list[2][0] or board_list[0][1]==board_list[1][1]==board_list[2][1] or board_list[0][2]==board_list[1][2]==board_list[2][2]):
        return("win")
    #diagnol checking
    if(board_list[0][0]==board_list[1][1]==board_list[2][2] or board_list[0][2]==board_list[1][1]==board_list[2][0]):
        return("win")
    else:
        return("lose")



#Code starts from here 
print("Two player tic tac toe game")
board_list=[[1,2,3],[4,5,6],[7,8,9]]
board_print(board_list)
print("Select the number where you want to mark in your turn")
print("Player 1 has 0 as its mark")
print("Player 2 has X as its mark")
print()
player_1="lose"
player_2="lose"
total_turns=0
while(player_1=="lose" and player_2=="lose"):
    if(total_turns==9):
        print("Game ended on a tie")
        break
    print("Player 1's turn :",end="")
    total_turns+=1
    player_1_input=int(input())
    update_board_list(player_1_input,board_list,1)
    player_1=check(board_list)
    if(player_1=="win"):
        print("Player 1 wins")
        break
    if(total_turns==9):
        print("Game ended on a tie")
        break
    print("Player 2's turn :",end="")
    total_turns+=1
    player_2_input=int(input())
    update_board_list(player_2_input,board_list,2)
    player_2=check(board_list)
    if(player_2=="win"):
        print("Player 2 wins")
        break