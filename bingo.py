from random import randint
import random

class Bingo():
    def __init__(self, numberPlayers):
        self.numberPlayers = numberPlayers

    # Creates a dictionary with all players and their cartons.
    def __playersCartons(self):
        players_dict = {}
        userEntry = self.numberPlayers
        if userEntry.isdigit():
            userEntry = int(userEntry)
            if userEntry < 1 or userEntry > 1000000:
                return "invalidRange"
            for player in range(1, userEntry+1):
                players_dict[player] = self.__createPlayerCarton()
            return players_dict
        else:
            return "noDigit"

    # Creates an individual carton for each player.
    def __createPlayerCarton(self):
        carton = []
        while len(carton) < 16:
            randomNumber = randint(1, 99)
            if not randomNumber in carton:
                carton.append(randomNumber)
        return carton

    # Starts the Bingo
    def bingoRound(self):
        players = self.__playersCartons()
        if players == "noDigit":
            return "That's not a valid entry. Please, type a number."
        if players == "invalidRange":
            return "That number is not within the valid range."
        bingoNumbers = [number for number in range(1, 100)]
        winners = []
        while len(bingoNumbers) > 0:
            randomNumber = random.choice(bingoNumbers)
            bingoNumbers.remove(randomNumber)
            print('The chosen number is {}'.format(randomNumber))
            for user in players:
                if randomNumber in players[user]:
                    players[user].remove(randomNumber)
                    if len(players[user]) == 0:
                        winners.append(str(user))
            if len(winners) > 0:
                if len(winners) == 1:
                    return "Player {} is the winner!".format(winners[0])
                else:
                    f_string = ", ".join(winners)
                    return "Players {} have won the Bingo!".format(f_string)


# b = Bingo(input("Give me a number between 1 and 1000000: "))
# print(b.bingoRound())