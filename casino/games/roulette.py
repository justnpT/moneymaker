import random

number_colours = {
"red": (1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36),
"black": (2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35)}

number_state = {
"even": (2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36),
"odd": (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35) }

bets = ("red", "black", "green", "even", "odd")

class roulette():

    result = None

    def roll(self):
        '''
        return one of 1 - 36
        :return:
        '''
        self.result = random.randint(0,36)

    def set_result(self, result):
        self.result = result

    def get_result(self, bet_type):
        if bet_type == "number":
            return self.get_number_result()
        elif bet_type == "colour":
            return self.get_colour_result()

    def get_number_result(self):
        return self.result

    def get_colour_result(self):
        for key in number_colours:
            if self.result in number_colours[key]:
                return key

    def get_multiplier(self, key):
        multiplier = {'number': 10, 'colour': 2}

        return multiplier[key]

    def bet(bet):
        """
        make a bet, roll the reoulette and return true if your bet passed
        """
        result = roulette.roll()
        if bet==bets[0]:
            return result in red
        elif bet==bets[1]:
            return result in black
        elif bet==bets[2]:
            return result in green
        elif bet==bets[3]:
            return result in even
        elif bet==bets[4]:
            return result in odd
        else:
            return False