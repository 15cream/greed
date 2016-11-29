from player import player
import random
class Game():
    def __init__(self):
        self.innings = 0
        self.game_status = True
        self.players = dict()
        self.players_in = []
        for p in xrange(5):
            self.players[p] = player(p)


    def cal_w(self, dices):
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
                    dices_used += 1
                if i == 5:
                    score += 50
                    dices_used += 1
        print dices, 'score:', score
        return [score, dices_used]

    def cal(self, dices):
        score = 0
        dices_used = 0
        for i in [2, 3, 4, 5, 6]:
            if dices.count(i) == 3:
                score += i * 100
                dices_used += 3
            elif dices.count(i) == 6:
                score += i * 100 * 2
                dices_used += 3
        score += [0, 100, 200, 1000, 1100, 1200, 3000][dices.count(1)]
        dices_used += dices.count(1)
        score += [0, 50, 100, 500, 550, 600, 1000][dices.count(5)]
        dices_used += dices.count(5)
        print dices, 'score:', score
        return [score, dices_used]



    def begin(self):
        print "Game start"
        while self.game_status:
            self.innings += 1
            print("\n--------------- round %d --------------\n" %(self.innings, ))
            for id, p in self.players.items():
                print("Player %d, status: %s" % (id, p.status))
            if len(self.players_in) < 6:
                self.in_or_out()
            self.game_in()
            print("\n--------------- round %d over-------------\n" %(self.innings, ))
        print "Game over"

    def in_or_out(self):
        print("\n---------------In or Out---------------\n")
        for id, p in self.players.items():
            if p.status == 'Out':
                [score, dices_used] = self.cal(p.dicing())
                if score >= 300:
                    p.status = 'In'
                    self.players_in.append(id)
                    p.score += score
                    print("Player %d : score %d, game in" %(id, score))

    def game_in(self):
        print("\n--------------- round begin--------------\n")
        for id in self.players_in:
            print("Player %d, total: %d" % (id, self.players[id].score))
        for id in self.players_in:
            player = self.players[id]
            player.dices_count = 6
            round_score = 0
            print(">>>>>>>>>>>>>>>>>>Player %d <<<<<<<<<<<<<<<<<<<<" % (id, ))
            while(True):
                [score, dices_used] = self.cal(player.dicing())
                if not score:
                    round_score = 0
                    print("Score 0, wait for next round")
                    break
                else:
                    player.dices_count -= dices_used
                    round_score += score
                    if player.score + round_score >= 3000:
                        self.game_status = False
                        player.score += round_score
                        print("Winner!!! round_score: %d, total: %d" % (round_score, player.score))
                        break
                    if player.dices_count:
                        if input('continue[0] or stop[1]'):
                            player.score += round_score
                            break
                    else:
                        player.score += round_score
                        print("No dices, wait for next round")
                        break
            print("total: %d, round_score: %d" % (player.score, round_score))
            # a new winner, game over
            if not self.game_status:
                break

Game().begin()
