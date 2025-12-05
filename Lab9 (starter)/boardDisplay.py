"""
Author: Prof. Alyssa
Description: Creates and displays the graphics
    based on the current state of the board.

Assignment adapted from HMC CS60

Author: Francisco Hernandez Jr.
Date: November 16, 2025
The BoardDisplay of the game, including drawing the board, snake, and food.
"""

import pygame
from preferences import Preferences

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = None

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """
        
        # Clear the board
        self.clear()

        # Draw the board
        # TODO Add your code to draw the board here!
        #Boarder drawn around the game area
        for row in range(Preferences.NUM_CELLS_TALL):
            for col in range(Preferences.NUM_CELLS_WIDE):
                cell = gameData.getCell(row, col)
                self.drawSquare(cell)
        # You may find the below drawSquare method helpful

        # Display the score
        self.displayScore(gameData)

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()

        # Draw the timer
        self.drawTimer(gameData)

        # Update the display
        pygame.display.update()

    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):
        """ Draws a cell-sized square at the given location.
            Inputs: cell - the Cell to draw """
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(self.__display, cellColor, [col*Preferences.CELL_SIZE, row*Preferences.CELL_SIZE, 
                                                     Preferences.CELL_SIZE, Preferences.CELL_SIZE])

    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = ((col*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
                            (row*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2))
        # Place the image on the display
        self.__display.blit(image, imageRect)

    def displayGameOver(self):
        """ Displays the game over message """

        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)

    def displayScore(self, gameData):
        """ Displays the current score on the screen """
        
        # Create the text
        scoreText = "Score: " + str(gameData.getScore())
        textSurface = Preferences.SCORE_FONT.render(scoreText, True, Preferences.SCORE_COLOR)
        # Place the score text on the display
        self.__display.blit(textSurface, Preferences.SCORE_LOCATION)

    def drawTimer(self, gameData):
        """ Draws the elapsed time in the top right corner """
    
        # Format the time
        totalSeconds = gameData.getTime()
        minutes = totalSeconds // 60
        seconds = totalSeconds % 60
        timeText = f"Time: {minutes}:{seconds:02d}" # :02d ensures "05" instead of "5"
        # Render the text
        textSurface = Preferences.TIMER_FONT.render(timeText, True, Preferences.TIMER_COLOR)
        # Calculate position (Top Right)
        textRect = textSurface.get_rect()
        textRect.topright = (Preferences.GAME_BOARD_WIDTH - 25, 20) # 10px padding
        # 4. Draw
        self.__display.blit(textSurface, textRect)