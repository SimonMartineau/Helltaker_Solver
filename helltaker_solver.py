from classes import *
from levels import *

"""
Equivalent solutions are reduced to one solution.
The different solutions found all leave a different board state.

Optimisation ideas:
    //Quit paths that are too far from the goal.
    //Reduce function calls.
    Use tuples instead of lists for the grid.
    
"""


Game = Helltaker(Level_1_HP, Level_1_Grid)
Game.solve()
Game.print_solutions()
Game.print_analysis()
Game.print_solution_grid()











