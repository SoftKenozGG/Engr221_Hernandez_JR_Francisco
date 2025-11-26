"""
Author: Prof. Alyssa
The Controller of the game, including handling key presses
(and AI in the next assignment). You will update this file.

Adapted from HMC CS60

Author: Francisco Hernandez Jr.
Date: November 16, 2025
The Controller of the game, including handling key presses
"""

from preferences import Preferences
from gameData import GameData
from boardDisplay import BoardDisplay

import pygame
from enum import Enum
from queue import Queue

class Controller():
    def __init__(self):
        # The current state of the board
        self.__data = GameData()
        # The display
        self.__display = BoardDisplay()
        # How many frames have passed
        self.__numCycles = 0


        # Attempt to load any sounds and images
        try:
            pygame.mixer.init()
            self.__audioEat = pygame.mixer.Sound(Preferences.EAT_SOUND)
            self.__display.headImage = pygame.image.load(Preferences.HEAD_IMAGE)
        except:
            print("Problem error loading audio / images")
            self.__audioEat = None


        # Initialize the board for a new game
        self.startNewGame()
        
    def startNewGame(self):
        """ Initializes the board for a new game """

        # Place the snake on the board
        self.__data.placeSnakeAtStartLocation()

    def gameOver(self):
        """ Indicate that the player has lost """
        self.__data.setGameOver()

    def run(self):
        """ The main loop of the game """

        # Keep track of the time that's passed in the game 
        clock = pygame.time.Clock()

        # Loop until the game ends
        while not self.__data.getGameOver():
            # Run the main behavior
            self.cycle() 
            # Sleep
            clock.tick(Preferences.SLEEP_TIME)

    def cycle(self):
        """ The main behavior of each time step """

        # Check for user input
        self.checkKeypress()
        # Update the snake state
        self.updateSnake()
        # Update the food state
        self.updateFood()
        # Increment the number of cycles
        self.__numCycles += 1
        # Update the display based on the new state
        self.__display.updateGraphics(self.__data)

    def checkKeypress(self):
        """ Update the game based on user input """
        # Check for keyboard input
        for event in pygame.event.get():
            # Quit the game
            if event.type == pygame.QUIT:
                self.gameOver()
            # Change the snake's direction based on the keypress
            elif event.type == pygame.KEYDOWN:
                # Reverse direction of snake
                if event.key in self.Keypress.REVERSE.value:
                    self.reverseSnake()
                # Enter AI mode
                elif event.key in self.Keypress.AI.value:
                    self.__data.setAIMode()
                # Change directions based on keypress if key is valid
                # Directions: up
                elif event.key in self.Keypress.UP.value:
                    self.__data.setDirectionNorth()
                # Directions: down
                elif event.key in self.Keypress.DOWN.value:
                    self.__data.setDirectionSouth()
                # Directions: left
                elif event.key in self.Keypress.LEFT.value:
                    self.__data.setDirectionWest()
                # Directions: right
                elif event.key in self.Keypress.RIGHT.value:
                    self.__data.setDirectionEast()

                

    def updateSnake(self):
        """ Move the snake forward one step, either in the current 
            direction, or as directed by the AI """

        # Move the snake once every REFRESH_RATE cycles
        if self.__numCycles % Preferences.REFRESH_RATE == 0:
            # Find the next place the snake should move
            if self.__data.inAIMode():
                nextCell = self.getNextCellFromBFS()
            else:
                nextCell = self.__data.getNextCellInDir()
            try:
                # Move the snake to the next cell
                self.advanceSnake(nextCell)
            except:
                print("Failed to advance snake")

    def advanceSnake(self, nextCell):
        """ Update the state of the world to move the snake's head to the given cell """

        # If we run into a wall or the snake, it's game over
        if nextCell.isWall() or nextCell.isBody():
            self.gameOver()
        
        # If we eat food, update the state of the board
        # TODO Tell __data that we ate food!
        # Snake should grow by one cell after eating food
        elif nextCell.isFood():
            self.playSound_eat()
            self.__data.moveSnakeToCellAndGrow(nextCell)
        
        # Otherwise, just move the snake forward
        # Snake should remain the same length after moving
        elif nextCell.isEmpty():
            self.__data.moveSnakeToCell(nextCell)

        # TODO Possibly add code here, using the helper methods
        # in gameData.py under the "snake movement methods" header

    def updateFood(self):
        """ Add food every FOOD_ADD_RATE cycles or if there is no food """
        if self.__data.noFood() or (self.__numCycles % Preferences.FOOD_ADD_RATE == 0):
            self.__data.addFood()

    def getNextCellFromBFS(self):
        """ Uses BFS to search for the food closest to the head of the snake.
            Returns the *next* step the snake should take along the shortest path
            to the closest food cell. """

        # Prepare all the tiles to search
        self.__data.resetCellsForSearch()

        # Initialize a queue to hold the tiles to search
        cellsToSearch = Queue()

        # Add the head to the queue and mark it as added
        head = self.__data.getSnakeHead()
        head.setAddedToSearchList()
        cellsToSearch.put(head)

        # Perform the BFS to find the food
        foodCell = None

        while not cellsToSearch.empty():
            # Get the next cell to search
            currentCell = cellsToSearch.get()

            # Check if we found food
            if currentCell.isFood():
                foodCell = currentCell
                break

            # Check all neighbors
            for neighbor in self.__data.getNeighbors(currentCell):
                #Ignore walls and snake body
                if neighbor.isWall() or neighbor.isBody():
                    continue

                # Ignore cells already added to the search list
                if neighbor.alreadyAddedToSearchList():
                    continue

                neighbor.setAddedToSearchList()
                neighbor.setParent(currentCell)
                cellsToSearch.put(neighbor)

        # If we found food, trace back to find the first cell in the path
        if foodCell:
            return self.getFirstCellInPath(foodCell)

        # If the search failed, return a random neighbor
        return self.__data.getRandomNeighbor(head)

    def getFirstCellInPath(self, foodCell):
        """ Takes the found food cell as input, and traces back
            to find the first cell in the path from the snake's head to the food.
            Returns that cell."""
        
        current = foodCell

        # Trace back from the food cell to find the first cell in the path
        while current.getParent():
            parent = current.getParent()
            if parent.isHead():
                return current
            
            current = parent
        return current
    
    def reverseSnake(self):
        """ Reverse the direction that the snake is moving, switching head and tail
            by pressing the 'r' key.
        """
        self.__data.reverseSnakeDirection()


    def playSound_eat(self):
        """ Plays an eating sound """
        if self.__audioEat:
            pygame.mixer.Sound.play(self.__audioEat)
            pygame.mixer.music.stop()

    class Keypress(Enum):
        """ An enumeration (enum) defining the valid keyboard inputs 
            to ensure that we do not accidentally assign an invalid value.
        """
        UP = pygame.K_i, pygame.K_UP        # i and up arrow key
        DOWN = pygame.K_k, pygame.K_DOWN    # k and down arrow key
        LEFT = pygame.K_j, pygame.K_LEFT    # j and left arrow key
        RIGHT = pygame.K_l, pygame.K_RIGHT  # l and right arrow key
        REVERSE = pygame.K_r,               # r
        AI = pygame.K_a,                    # a


if __name__ == "__main__":
    Controller().run()