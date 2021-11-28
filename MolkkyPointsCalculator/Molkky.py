

"!!!!!!!!!!!!!!!!!!!!"
"ONLY CLASS PLAYER IS MY CREATION. THE MAIN METHOD IS NOT MADE BY ME!"
"!!!!!!!!!!!!!!!!!!!!"



class Player:
    """Class player. Implements a player who is playing Mölkky and
    keeps score of the players points and provides different methods
    to it.
    """

    def __init__(self, name):
        """Constructor of a player object.

        :param name: string, name given to the player
        :param points: int, the points of the player
        :param throws: int, if the throw doesn't miss this is incremented by 1
        :param pt_history: list, creates a list to keep track of players points
        in the previous rounds.
        """

        self.__name = name
        self.__points = 0
        self.__throws = 0
        self.__pt_history = []

    def get_name(self):
        """Returns the name of the player

        :return: string, name of the player
        """

        return self.__name

    def add_points(self, points):
        """Adds points to the player's name.

        :param points: int, the points to be added
        """

        self.__points += points
        self.__pt_history.append(points)

        if points > 0:
            self.__throws += 1

        if 39 < self.__points < 50:
            print(f"{self.__name} needs only {50 - self.__points} points. It's "
                  f"better to avoid knocking down the pins with higher points.")

        if self.__points > 50:
            self.__points = 25
            print(self.__name, "gets penalty points!")

    def has_won(self):
        """If the player has fifty points he is the winner.

        :return: True if points are equal to 50
        """

        if self.__points == 50:
            return True

    def get_points(self):
        """Returns the points of a player
        :param: int, returns the points
        """

        return self.__points

    def calculate_average(self):
        """Calculates the average of all the points the player has
        accumulated in the game.

        :return: float, returns the average
        """

        sum = 0
        for point in self.__pt_history:
            sum += point

        return sum / len(self.__pt_history)

    def get_shot_accuracy(self):
        """Calculates the shot accuracy of a player

        :return: returns the shot accuracy
        """

        if len(self.__pt_history) == 0:
            return 0.0
        return self.__throws / len(self.__pt_history) * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.calculate_average() < pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()}"
              f" p, hit percentage {player1.get_shot_accuracy():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()}"
              f" p, hit percentage {player2.get_shot_accuracy():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
