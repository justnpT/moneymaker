class Prices:

    def __init__(self):
        self.prices = []

    def set_current_price(self, price):
        self.prices.append(price)

    def get_last_price(self):
        return self.prices[-1:][0]

    def get_all_prices(self):
        return self.prices

    def is_empty(self):
        if self.prices:
            return False
        else:
            return True
