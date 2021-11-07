import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    #check horizontals
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} wins horizontally!")
            return True
    
    #check verticals
    for col in range(len(current_game)):
        verts = []
        for row in current_game:
            verts.append(row[col])

        if all_same(verts):
            print(f"Player {verts[0]} wins vertically!")
            return True
    
    #check forward diagonal
    diags = []
    for index in range(len(current_game)):
        diags.append(current_game[index][index])
    
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally!")
        return True

    #check backward diagonal
    bdiags = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        bdiags.append(current_game[row][col])
    
    if all_same(bdiags):
        print(f"Player {bdiags[0]} wins diagonally!")    
        return True
    
    #no win condition met, return false
    return False


def execute_move(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is already occupied, Choose another!")
            return False
        if not just_display and game_map[row][column] == 0:
            game_map[row][column] = player
        elif not just_display:
           print("Error: not a playable field")

        print("   0  1  2")
        for count,row in enumerate(game_map):
            print(count, row) 
        #win(game_map)
        return True
    except IndexError as e:
        print("Error: did you input row/column as 0,1,2", e)
        return False
    except Exception as e: 
        print("Something went wrong!", e)
        return False

play = True
players = [1, 2]
while play: 
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    game_won = False
    execute_move(game, just_display=True)
    player_choice = itertools.cycle(players)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player is: {current_player}")
        played = False
        while not played:
            try:
                column_choice = int(input("What column do you want to play? (0, 1, 2): "))
                row_choice = int(input("What row do you want to play? (0, 1, 2): "))
                played = execute_move(game, current_player, row_choice, column_choice)
            except Exception as e:
                print("Something went wrong!", e)
        if win(game):
            game_won = True
            again = input("wanna try again? y/n ")
            if again.lower() == "y":
                print("restarting")
            else: 
                print("bye!")
                play = False
            