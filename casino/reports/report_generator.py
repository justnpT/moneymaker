from casino.games.roulette import roulette

class report_generator():

    loggingEnabled = True;

    @staticmethod
    def log_game(roll_number):
        if report_generator.loggingEnabled == True:
            print("game: "+ str(roll_number))

    @staticmethod
    def log_result(result):
        if report_generator.loggingEnabled == True:
            print("result: "+str(result))

    @staticmethod
    def log_player_bet(player_bet):
        if report_generator.loggingEnabled == True:
            for bet_type, bet_dict in player_bet.iteritems():
                print("bet type: "+bet_type),
                for bet_target, bet_amount in bet_dict.iteritems():
                    if type(bet_target) == str:
                        print(bet_target+": "+str(bet_amount)),
                    elif type(bet_target) == int:
                        print(str(bet_target)+ ": "+str(bet_amount)),
                print("")
                print("bet multiplier: " + str(roulette.get_multiplier(bet_type)))

    @staticmethod
    def log_player_account(player_account):
        print("player account: "+str(player_account))

    @staticmethod
    def log_player_account_history(player_account_history):
        print("player account history: "),
        for account in player_account_history:
            print(str(account)+", "),
        print("")

    def log_multiplier(multiplier):
        print("multiplier: "+multiplier)

    def log_profit(profit):
        print("profit: "+profit)



    def printReport(self):
        for key, value in self.rolls.iteritems():
            for key2, value2, in value:
                print("roll: "+key2, "result: "+value2["result"], "multiplier "+value2["multiplier"],
                      "profit: "+value2["profit"], "player_account: "+value2["player_account"])