import random

class player():
    def __init__(self, p):
        self.id = p
        self.score = 0
        self.status = 'Out'
        self.dices_count = 6

    def dicing(self):
        dices = []
        for i in xrange(self.dices_count):
            dices.append(random.randint(1, 6))
        return dices