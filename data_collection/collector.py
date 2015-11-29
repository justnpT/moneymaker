import logging
logging.basicConfig()
import condition.buying_condition


def collect_trade(data, instance_prices):
    """
    The function collects the data that comes from the market

    :param data: The data that comes from the market and contains fields
    :param instance_prices: Instance of price
    """
    price_key = u'price'

    current_trade_price = data[price_key]
    if instance_prices.is_empty():
        last_trade_price = current_trade_price
    else:
        last_trade_price = instance_prices.get_last_price()
    instance_prices.set_current_price(current_trade_price)
    print("last trade price: " + str(last_trade_price) + ", current trade price: " + str(current_trade_price))