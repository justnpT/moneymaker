__author__ = 'wikia'
"""
croupier supervises the relation between casino and client
"""

class croupier():
    """
    croupier has two states:
    states: no more bets, waiting for bets
    """


    from play.player import player

    # lista ktora zawiera slowniki odpowiadajce graczom:
    # {name: player_name, bet: bet}
    players = []


    def get_amounts(self, amounts):
        '''
        :param amounts: {numbers: amount (int), colours: amount (int)}
        :return:
        '''
        pass

    def welcome_player(self, player):
        self.players.append(player)

    def verify_match(self, bet_type, roulette, player):
        """ pay player if bet_type wins, and take money from player bet if bet_type doesn't win"""
        result = roulette.get_result(bet_type)
        payment = 0

        for key in player.get_bet()[bet_type].copy():
            if key == result:
                payment += player.get_bet()[bet_type][key] * roulette.get_multiplier(bet_type)
            else:
                player.get_bet()[bet_type][key] = 0
        return payment

    def verify_number_match(self, roulette, player):
        return self.verify_match("number", roulette, player)

    def verify_colour_match(self, roulette, player):
        return self.verify_match("colour", roulette, player)

    def pay(self, player, payment):
        player.set_payment(payment)

    def verify_matches(self, roulette, player):
        '''
        Check if player the result is winning any of the player bets
        :param result:
        :return:
        '''
        payment = 0
        payment += self.verify_number_match(roulette, player)
        payment += self.verify_colour_match(roulette, player)
        self.pay(player, payment)