from collections import Counter

class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for _ in range(self.matches):
            p1_puts = player1.put_candy()
            p2_puts = player2.put_candy()

            if p1_puts and p2_puts:
                self.registry[player1.name] += 2
                self.registry[player2.name] += 2
                player1.get_candy(2)
                player2.get_candy(2)
            elif p1_puts and (not p2_puts):
                self.registry[player1.name] -= 1
                self.registry[player2.name] += 3
                player1.get_candy(0)
                player2.get_candy(3)
            elif (not p1_puts) and p2_puts:
                self.registry[player1.name] += 3
                self.registry[player2.name] -= 1
                player1.get_candy(3)
                player2.get_candy(0)
            elif (not p1_puts) and (not p2_puts):
                player1.get_candy(0)
                player2.get_candy(0)


    def top3(self):
        for name, score in self.registry.most_common(3):
            print(f"{name} {score}")
