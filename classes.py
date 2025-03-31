class Helltaker:
    def __init__(self, HP, Game_Grid):
        self.States_List = [Game_State(Game_Grid, HP)]
        self.Solutions = []


    def solve(self):
        # Phase 1) Generate all possible game states
        # Continue while there is at least one unplayed state in self.States.
        while any(not state.Played for state in self.States_List):
            # Iterate over a copy of self.States to safely add new states during the loop.
            for state in list(self.States_List):
                if not state.Played:
                    new_states_list = state.next_turn()
                    for new_state in new_states_list:
                        # Check if the new state is already in self.States_List.
                        if not any(new_state.Game_Grid == existing_state.Game_Grid for existing_state in self.States_List):
                            # If not, add it to self.States_List.
                            self.States_List.append(new_state)

                    # Mark this state as played so it won't be processed again.
                    state.Played = True

        # Phase 2) Check if any game states are solved
        for Game_State in self.States_List:
            if Game_State.Solved == True:
                self.Solutions.append(Game_State.Instructions)

    def print_solutions(self):
        print("Number of solutions: ", len(self.Solutions))
        for i in range(0, len(self.Solutions)):
            print("Solution ", i + 1, ":")
            print(self.Solutions[i])
        print("Number of generated states: ", len(self.States_List))

    


class Game_State:
    def __init__(self, Game_Grid, HP):
        self.Game_Grid = Game_Grid
        self.HP = HP
        self.Instructions = []
        self.Played = False
        self.Solved = False
        self.has_key = False


    def next_turn(self):
        possible_moves = ['up', 'down', 'left', 'right']
        new_states_list = []
        for move in possible_moves:
            new_state = self.copy_state()
            if new_state.player_move(move):
                new_state.Instructions.append(move)
                # Check if the new state is solved
                if new_state.Game_Grid[new_state.get_player_pos()[0]+1][new_state.get_player_pos()[1]] == 'G' or new_state.Game_Grid[new_state.get_player_pos()[0]-1][new_state.get_player_pos()[1]] == 'G' or new_state.Game_Grid[new_state.get_player_pos()[0]][new_state.get_player_pos()[1]+1] == 'G' or new_state.Game_Grid[new_state.get_player_pos()[0]][new_state.get_player_pos()[1]-1] == 'G':
                    new_state.Solved = True
                new_states_list.append(new_state)
        return new_states_list
    

    def copy_state(self):
        new_game_grid = [row[:] for row in self.Game_Grid]
        new_state = Game_State(new_game_grid, self.HP)
        new_state.Instructions = self.Instructions[:]
        new_state.Played = False
        new_state.Solved = False
        new_state.has_key = self.has_key
        return new_state


    def get_player_pos(self):
        for i in range(len(self.Game_Grid)):
            for j in range(len(self.Game_Grid[i])):
                if self.Game_Grid[i][j] == 'P':
                    return (i, j)
                
    def get_goal_pos(self):
        for i in range(len(self.Game_Grid)):
            for j in range(len(self.Game_Grid[i])):
                if self.Game_Grid[i][j] == 'G':
                    return (i, j)   
                

    def get_distance_to_goal(self):
        player_i, player_j = self.get_player_pos()
        goal_i, goal_j = self.get_goal_pos()
        return abs(player_i - goal_i) + abs(player_j - goal_j)


    def player_move(self, direction):
        """
        //If there is a wall in the way, return False.
        //If there is an empty space that way, move there.
        If there is a block in the way, push it unless it is blocked by a block, skeleton or wall.
        If there is a skeleton in the way, skeleton gets pushed back.
        If the skeleton is pushed into a wall or block or another skeleton, it disappears.
        //If there is a key in the way, pick it up.
        //If there is a chest in the way, it disappears.
        //If there is a goal in the way, Solved = True.
        //HP goes down by 1 for every move.
        //If HP goes below 0, return False.
        If there is a spike ...

        Return True for valid move.
        Return False for invalid move.
        """

        i, j = self.get_player_pos()

        if direction == 'up':
            new_i, new_j = i - 1, j
            new_i2, new_j2 = i - 2, j
        elif direction == 'down':
            new_i, new_j = i + 1, j
            new_i2, new_j2 = i + 2, j
        elif direction == 'left':
            new_i, new_j = i, j - 1
            new_i2, new_j2 = i, j - 2
        elif direction == 'right':
            new_i, new_j = i, j + 1
            new_i2, new_j2 = i, j + 2

        # Decrease HP
        self.HP -= 1  # Decrease HP by one
        if self.HP < 0:
            return False

        # Check for walls
        if self.Game_Grid[new_i][new_j] == 'W':
            return False

        # Check for empty space
        if self.Game_Grid[new_i][new_j] == 'E':
            self.Game_Grid[i][j] = 'E'
            self.Game_Grid[new_i][new_j] = 'P'
            return True

        # Check for keys
        if self.Game_Grid[new_i][new_j] == 'K':
            self.Game_Grid[i][j] = 'E'
            self.Game_Grid[new_i][new_j] = 'P'
            self.has_key = True
            return True
        
        # Check for chests
        if self.Game_Grid[new_i][new_j] == 'C':
            if self.has_key:
                self.Game_Grid[i][j] = 'E'
                self.Game_Grid[new_i][new_j] = 'P'
                return True
            else:
                return False
            
        # Check for skeletons
        if self.Game_Grid[new_i][new_j] == 'S':
            # Check if the skeleton can be pushed
            if self.Game_Grid[new_i2][new_j2] == 'E':
                self.Game_Grid[i][j] = 'P'
                self.Game_Grid[new_i][new_j] = 'E'
                self.Game_Grid[new_i2][new_j2] = 'S'
                return True
            elif self.Game_Grid[new_i2][new_j2] == 'W' or self.Game_Grid[new_i2][new_j2] == 'B' or self.Game_Grid[new_i2][new_j2] == 'S':
                self.Game_Grid[new_i][new_j] = 'E'
                return True
            
        # Check for blocks
        if self.Game_Grid[new_i][new_j] == 'B':
            # Check if the block can be pushed
            if self.Game_Grid[new_i2][new_j2] == 'E':
                self.Game_Grid[i][j] = 'P'
                self.Game_Grid[new_i][new_j] = 'E'
                self.Game_Grid[new_i2][new_j2] = 'B'
                return True
            elif self.Game_Grid[new_i2][new_j2] == 'W' or self.Game_Grid[new_i2][new_j2] == 'B' or self.Game_Grid[new_i2][new_j2] == 'S':
                return True


        
