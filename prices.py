class Prices:
    last_price = None

    def __init__(self):
        self.last_price = None

    def set_current_price(self, price):
        self.last_price = price

    def get_last_price(self):
        return self.last_price

