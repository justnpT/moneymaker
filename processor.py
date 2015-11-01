import logging
logging.basicConfig()

def process_trade(data, instance_prices):
    price_key = u'price'

    current_trade_price = data[price_key]
    if instance_prices.get_last_price() is None:
        last_trade_price = current_trade_price
    else:
        last_trade_price = instance_prices.get_last_price()
    instance_prices.set_current_price(current_trade_price)
    print("last trade price: " + str(last_trade_price) + ", current trade price: " + str(current_trade_price))