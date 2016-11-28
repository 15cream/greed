from player import player
import random
class Game():
    def __init__(self):
        self.innings = 0
        self.players = dict()
        self.players_in = []
        for p in xrange(5):
            self.players[p] = player(p)


    def cal(self, dices):
        score = 0
        dices_used = 0
        if dices.count(1) == 6:
            return [3000, 6]
        for i in range(1, 7):
            if dices.count(i) == 3:
                if i == 1:
                    score += 1000
                else:
                    score += i * 100
                dices_used += 3
            if dices.count(i) == 1:
                if i == 1:
                    score += 100
                if i == 5:
                    score += 50
                dices_used += 1
        return [score, dices_used]




    def begin(self):
        print "Game start"
        print 'Player profiles:'
        for id, p in self.players.items():
            print("Player %d : score %d" %(id, p.score))

        while(True):
            self.innings += 1
            print("--------------- round %d begin------------" %(self.innings, ))
            self.in_or_out()
            print("--------------- round %d over-------------" %(self.innings, ))
            if input("another round[0] or exit[1]?"):
                break
        print "Game over"

    def in_or_out(self):
        for id, p in self.players.items():
            [score, dices_used] = self.cal(p.dicing())
            if score >= 300:
                p.status = 'In'
                self.players_in.append(id)
            print("Player %d : score %d, %s" %(id, score, p.status))

    def game_in(self):
        for id in self.players_in:
            pass



Game().begin()
