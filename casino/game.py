from casino.reports.report_generator import report_generator

"""
Elementy gry: gracze, strategia gracza, krupier, ruletka
"""

from play.player import player
from play.strategy import strategy
from croupier import croupier
from games.roulette import roulette


from itertools import combinations_with_replacement
n = [k for k in range(0, 9)]
k = 3
games = list(combinations_with_replacement(n, k))

"""
profit_3_3, three incomes, profitable strategy
profit_3_2, two incomes, profitable strategy
profit_3_1, one income, profitable strategy

noprofit_3_2, two incomes, inprofitable strategy
noprofit 3_1, one incomes, inprofitable strategy
noprofit_3_0, zero income, inprofitable strategy
"""

profit_3_3 = []
profit_3_2 = []
profit_3_1 = []

roulette = roulette()

croupier = croupier()
profit_sum = 0
game_number = 0;

for result_series in games:
    game_number+=1

    player_strategy = strategy(roulette)
    player_michal = player("Michal", 50, player_strategy)
    profit_count = 0;
    first_account = player_michal.get_account()
    if result_series == (3, 4, 5):
        print "siemanko"
    for result in result_series:

        before = player_michal.get_account()
        croupier.add_player(player_michal)
        roulette.set_result(result) # ustawienie rezultatu stan ruletki i poznaje rezultat

        croupier.pay_for_matches(roulette, player_michal) # na podstawie rezultatu krupier wyplaca graczom kwoty

        player_michal.set_bet()

        if player_michal.get_account() > 0:
            print("")
            report_generator.log_game(game_number)
            report_generator.log_result(result)
            report_generator.log_player_bet(player_michal.get_bet())
            report_generator.log_player_account(player_michal.get_account())
            report_generator.log_player_account_history(player_michal.get_account_history())
            profit_sum += player_michal.get_account()
        else:
            break

        after = player_michal.get_account()
        if after > before:
            profit_count+=1
    if profit_count == 1 and first_account < player_michal.get_account():
        profit_3_1.append(player_michal.get_account())
    elif profit_count == 2 and first_account < player_michal.get_account():
        profit_3_2.append(player_michal.get_account())
    elif profit_count == 3 and first_account < player_michal.get_account():
        profit_3_3.append(player_michal.get_account())
    player_michal.get_account()

# import numpy
# a = numpy.mean(profit_3_3)
# b = numpy.mean(profit_3_2)
# c = numpy.mean(profit_3_1)

#TODO: czemu dla analogicznych strategii sa rozne wyniki np 12/1: 10, 3/15: 20/17, 15:20
#
# print("profit_3_3 mean:" +str(a))
# print("profit_3_2 mean:" +str(b))
# print("profit_3_1 mean:" +str(c))
# print("profit sum: "+str(profit_sum))
