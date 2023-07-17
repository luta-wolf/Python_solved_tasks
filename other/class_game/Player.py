from Behaviours import Behaviours


class Player(object):

    def __init__(self, name: str = "Player", candies: int = 0):
        self.candies = 0
        self.name = name
        self.behaviour = None
        self.original_behaviour = None
        self.behaviour_history = []

    def put_candy(self):
        put_amount = 0 if self.behaviour == Behaviours.Cheater else 1
        # self.candies -= put_amount
        return put_amount

    def get_candy(self, n):
        # self.candies += n
        self.change_behaviour(opponent_behaviour=Behaviours.Cheater if n == 0 else Behaviours.Cooperator)
        # return n

    def change_behaviour(self, opponent_behaviour):
        pass


class Cheater(Player):

    def __init__(self, name: str = "Cheeter", candies: int = 1):
        super().__init__(name, candies)
        self.behaviour = Behaviours.Cheater
        self.original_behaviour = Behaviours.Cheater


class Cooperator(Player):

    def __init__(self, name: str = "Cooperator", candies: int = 1):
        super().__init__(name, candies)
        self.behaviour = Behaviours.Cooperator
        self.original_behaviour = Behaviours.Cooperator


class Copycat(Player):

    def __init__(self, name: str = "Copycat", candies: int = 1):
        super().__init__(name, candies)
        self.behaviour = Behaviours.Cooperator
        self.original_behaviour = Behaviours.Copycat

    def change_behaviour(self, opponent_behaviour: int):
        self.behaviour = opponent_behaviour


class Grudger(Player):

    def __init__(self, name: str = "Grudger", candies: int = 1):
        super().__init__(name, candies)
        self.behaviour = Behaviours.Cooperator
        self.original_behaviour = Behaviours.Grudger

    def change_behaviour(self, opponent_behaviour: int):
        if opponent_behaviour == Behaviours.Cheater:
            self.behaviour = Behaviours.Cheater


class Detective(Player):
    def __init__(self, name: str = "Detective", candies: int = 1):
        super().__init__(name, candies)
        self.behaviour = Behaviours.Cooperator
        self.original_behaviour = Behaviours.Detective
        self.opponent_cheated = False

    def change_behaviour(self, opponent_behaviour: int):
        self.behaviour_history.append(self.behaviour)
        games_so_far = len(self.behaviour_history)
        if games_so_far == 1:
            self.behaviour = Behaviours.Cheater
        elif games_so_far > 1 and games_so_far < 4:
            self.behaviour = Behaviours.Cooperator
        elif games_so_far >= 4 and self.opponent_cheated:
            self.behaviour = opponent_behaviour
        elif games_so_far >= 4 and (not self.opponent_cheated):
            self.behaviour = Behaviours.Cheater

        if (not self.opponent_cheated) and opponent_behaviour == Behaviours.Cheater:
            self.opponent_cheated = True

        # if (not self.opponent_cheated) and games_so_far >= 4:
        #     self.behaviour = Behaviours.Cheater
