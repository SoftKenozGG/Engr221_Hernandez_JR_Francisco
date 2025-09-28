"""
Name: Francisco Hernandez JR
MazeSolver.py
Description: Find the path by depth-first-search
"""

import sys, os 
sys.path.append(os.path.dirname(__file__))

from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:

    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object (Stack or Queue)

    def tileIsVisitable(self, row, col):#Check if the tile is visitable
        tile = self.maze.contents[row][col]
        return  not tile.getIsWall() and not tile.isVisited()

    def solve(self):
        start = self.maze.start
        goal = self.maze.goal
        self.ss.add(start)
        while not self.ss.isEmpty():
            current = self.ss.remove()
            current.visit()
            if current == goal:
                return current
            row = current.getRow()
            col = current.getCol()

            # Check the tile north
            if row > 0 and self.tileIsVisitable(row - 1, col):
                north = self.maze.contents[row - 1][col]
                north.setPrevious(current)
                self.ss.add(north)
                
            # Check the tile south
            if row < self.maze.num_rows - 1 and self.tileIsVisitable(row + 1, col):
                south = self.maze.contents[row + 1][col]
                south.setPrevious(current)
                self.ss.add(south)

            # Check the tile to the east
            if col < self.maze.num_cols - 1 and self.tileIsVisitable(row, col + 1):
                east = self.maze.contents[row][col + 1]
                east.setPrevious(current)
                self.ss.add(east)

            # Check the tile to the west
            if col > 0 and self.tileIsVisitable(row, col - 1):
                west = self.maze.contents[row][col - 1]
                west.setPrevious(current)
                self.ss.add(west)

        return None

    # Get the path from Start to Goal as a list of tiles
    def getPath(self):
        path = []
        current = self.maze.goal
        while current is not None:
            path.append(current)
            current = current.getPrevious()
        return path

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["##____#_##",
                     "#____##__#",
                     "_S#_______",
                     "__##_____#",
                     "____####__",
                     "#____##___",
                     "#__##___#_",
                     "___##___##",
                     "#___#__G__",
                     "_______###",])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()