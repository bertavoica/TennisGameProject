class player:
    def __init__(self):
        self.score = 0
        self.game = 0
        self.sets = 0

    def rein(self):
        self.score = 0
        self.game = 0

    def reinscore(self):
        self.score = 0

    def updatescore(self, val):
        if self.score > 25:
            self.score += val
        else:
            self.score = 15
        return self.score

    def updategame(self):
        self.game += 1

    def updateset(self):
        self.sets += 1
