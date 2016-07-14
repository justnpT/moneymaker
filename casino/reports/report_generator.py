from PollyReports import Report, Band, Element
from reportlab.pdfgen.canvas import Canvas

class report_generator():

    def __init__(self):
        self.rolls = dict()
        {"result": [], "multiplier": [], "profit": [], "player account":[]}

    def log_roll(self, roll_number):
        self.rolls[roll_number] = dict()

    def log_result(self, roll_number, result):
        self.rolls[roll_number]["result"] = result

    def log_multiplier(self, roll_number, multiplier):
        self.rolls[roll_number]["multiplier"] = multiplier

    def log_profit(self, roll_number, profit):
        self.rolls[roll_number]["profit"] = profit

    def log_player_account(self, roll_number, player_account):
        self.rolls[roll_number]["player_account"] = player_account

    def printReport(self):
        for key, value in self.rolls.iteritems():
            for key2, value2, in value:
                print("roll: "+key2, "result: "+value2["result"], "multiplier "+value2["multiplier"],
                      "profit: "+value2["profit"], "player_account: "+value2["player_account"])