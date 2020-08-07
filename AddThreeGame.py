# Author: Makaliah Dickinson
# Date: 8/1/2020
# Description: Write a class called AddThreeGame that allows two players to play a game in which they alternately choose
#              numbers from 1-9. They may not choose a number that has already been selected by either player. If at any
#              point exactly three of the player's numbers sum to 15, then that player has won. If all numbers from 1-9
#              are chosen, but neither player has won, then the game ends in a draw.
#              The class will need private data members for:
#              keeping track of which numbers have been chosen, and by whom
#              the current state, which holds one of the four following values: "FIRST_WON", "SECOND_WON", "DRAW", or
#              "UNFINISHED"
#              keeping track of whose turn it is


class AddThreeGame:
    # Initialize the files
    def __init__(self):
        self.__p1 = 0
        self.__p2 = 0
        self.__played = []
        self.__str = "UNFINISHED"

    # return the current state
    def get_current_state(self):
        return self.__str

    # when a player makes a move
    def make_move(self, pl, x):
        if x in self.__played:
            return False
        if x > 9 or x < 1:
            return False
        if pl == "first":
            self.__pl = self.__p1 + x
            self.__played.append(x)
        elif pl == "second":
            self.__p2 = self.__p2 + x
            self.__played.append(x)
        if self.__p1 == 15 and self.__p2 == 15:
            self.__str = "DRAW"
        elif self.__p1 == 15:
            self.__str = "FIRST_WON"
        elif self.__p2 == 15:
            self.__str = "SECOND_WON"
        if len(self.__played) == 9:
            self.__str = "DRAW"
        return True


# Initialize the object for the class
game = AddThreeGame()
# Infinite loop till game is won or drawn
while True:
    x = int(input("Player 1 please enter a number: "))
    while True:
        if (game.make_move("first", x) == True):
            break
        else:
            x = int(input("Invalid input! Player 2 please re-enter a number: "))
# Check if game is over
playstatus = game.get_current_state()
if playstatus == "UNFINISHED":
    print("No one reached 15. Get ready for next round.\n")
elif playstatus == "FIRST_WON":
    print("First player won!!!\n")
elif playstatus == "SECOND_WON":
    print("Second player won!!!\n")
elif playstatus == "DRAW":
    print("Game ends in draw\n")
