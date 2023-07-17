from Game import Game
from Player import *


def main():
    game = Game()
    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Copycat())
    game.play(Cheater(), Detective())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Copycat())
    game.play(Cooperator(), Detective())
    game.play(Grudger(), Copycat())
    game.play(Grudger(), Detective())
    game.play(Copycat(), Detective())

    game.top3()


if __name__ == "__main__":
    main()
