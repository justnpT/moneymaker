import logging
import datetime
import os

def collect_trade(data):
    """
    The function collects the data that comes from the market in a file

    :param data: The data that comes from the market and contains fields
    """

    unix_timestamp = data[u'date']
    market = data[u'market']
    year_month_day = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d')

    raw_data_path = "../raw_data/"
    if not os.path.exists(raw_data_path):
        os.makedirs(raw_data_path)
    file = open(raw_data_path+year_month_day+"_"+market+"_trade", 'a')
    file.write(str(data) + '\n')