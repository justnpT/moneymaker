import datetime

def collect_trade(data):
    """
    The function collects the data that comes from the market in a file

    :param data: The data that comes from the market and contains fields
    """

    unix_timestamp = data[u'date']
    market = data[u'market']
    year_month_day = datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d')

    file = open("../raw_data/"+year_month_day+"_"+market+"_trade", 'a')
    file.write(str(data) + '\n')