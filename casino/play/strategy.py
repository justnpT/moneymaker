__author__ = 'wikia'


class strategy:

    results = []
    player_account = []
    player = None
    # bet = {"number": {}, "colour": {"red": None, "black": None}}
    roulette = None

    def get_bet_sum(self):
        sum = 0
        for key in self.bet:
            for key_2 in self.bet[key]:
               sum += self.bet[key][key_2]
        return sum

    def get_first_bet(self, player):
        ''' invoke before the first roll'''
        self.player_account.append(player.get_account())
        bid = player.get_account()/5
        self.bet["number"] = {8: 20, 16: 20, 3: 10}
        self.bet["colour"]["red"] = 0
        self.bet["colour"]["black"] = 0
        return self.bet

    def get_bet(self, player):
        return self.bet.copy()

    def __init__(self, roulette):
        self.roulette = roulette
        self.bet =  {"number": {}, "colour": {"red": None, "black": None}}
