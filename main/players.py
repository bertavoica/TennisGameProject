class Player:
    def __init__(self, position_x, position_y, dimension_x, dimension_y):
        self.score = 0
        self.game = 0
        self.sets = 0
        self.position_x = position_x
        self.position_y = position_y
        self.dimension_x = dimension_x
        self.dimension_y = dimension_y

    def rein(self):
        self.score = 0
        self.game = 0

    # reinitialise score
    def rein_score(self):
        self.score = 0

    def update_score(self, val):
        if self.score > 25:
            self.score += val
        else:
            self.score = 15
        return self.score

    def update_game(self):
        self.game += 1

    def update_set(self):
        self.sets += 1
