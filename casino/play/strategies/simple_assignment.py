__author__ = 'wikia'
from casino.play.strategy import strategy

class simple_10_20_20(strategy):

    def __init__(self, roulette):
        strategy.__init__(self, roulette)

    def get_first_bet(self, player):
        ''' invoke before the first roll'''
        self.player_account.append(player.get_account())
        bid = player.get_account()/5
        self.bet["number"] = {8: 20, 16: 20, 3: 10}
        self.bet["colour"]["red"] = 0
        self.bet["colour"]["black"] = 0
        return self.bet