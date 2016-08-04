__author__ = 'wikia'
import copy

class player():
    """
    Both play and croupier has a state
    play: betting, no more bets
    """

    # bet = {numbers: {x: amount, b: amount, c: amount}, colour: {red: amount, blue: amount} }
    name = ''
    account = 0
    strategy = None
    account_history = []

    def __init__(self, player_name, player_account, player_strategy):
        self.reset()
        self.name = player_name
        self.account = player_account
        self.account_history.append(self.account)
        self.strategy = player_strategy
        self.bet = copy.deepcopy(player_strategy.get_first_bet(self))
        self.account -= self.strategy.get_bet_sum()
        self.account_history.append(self.account)

    def reset(self):
        self.name = ''
        self.account = 0
        self.strategy = None
        self.account_history = []

    def set_bet(self):
        self.bet = copy.deepcopy(self.strategy.get_bet(self))
        # update account
        self.account -= self.strategy.get_bet_sum()
        self.account_history.append(self.account)

    def set_payment(self, payment):
        self.account += payment
        self.account_history.append(self.account)

    def get_name(self):
        return self.name

    def get_account(self):
        return self.account

    def get_account_history(self):
        return self.account_history

    def get_bet(self):
        return self.bet