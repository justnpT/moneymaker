"""
This file is responsible for gathering data to data structures.
This file is not responsible for any processing

An example for Python Socket.io Client
    Require installing socket.io client for Python first
    Refer to the source here to install socket.io client for Python: https://github.com/fuzeman/PySocketIO-Client
"""
import time
import json
import re
import hmac
import hashlib
import base64
from data_collection import collector
from data_collection.prices import Prices
try:
    from pip.util import get_installed_distributions
except:
    from pip.utils import get_installed_distributions
import pysocketio_client as io

access_key = "<YOUR ACCESS KEY>"
secret_key = "<YOUR SECRET KEY>"


def get_tonce():
    return int(time.time() * 1000000)


def get_postdata():
    post_data = {}
    tonce = get_tonce()
    post_data['tonce'] = tonce
    post_data['accesskey'] = access_key
    post_data['requestmethod'] = 'post'

    if 'id' not in post_data:
        post_data['id'] = tonce

    #modefy here to meet your requirement
    post_data['method'] = 'subscribe'
    post_data['params'] = ['order_cnybtc', 'order_cnyltc', 'order_btcltc', 'account_info']
    return post_data


def get_sign(pdict):
    pstring = ''
    fields = ['tonce', 'accesskey', 'requestmethod', 'id', 'method', 'params']
    for f in fields:
        if pdict[f]:
            if f == 'params':
                param_string = str(pdict[f])
                param_string = param_string.replace('None', '')
                param_string = re.sub("[\[\] ]", "", param_string)
                param_string = re.sub("'", '', param_string)
                pstring += f + '=' + param_string + '&'
            else:
                pstring += f + '=' + str(pdict[f]) + '&'
        else:
            pstring += f + '=&'
    pstring = pstring.strip('&')
    phash = hmac.new(secret_key, pstring, hashlib.sha1).hexdigest()

    return base64.b64encode(access_key + ':' + phash)

#logging.basicConfig(level=logging.DEBUG)
socket = io.connect('https://websocket.btcchina.com')


@socket.on('connect')
def connected():
    print("Connected!")


socket.emit('subscribe', 'marketdata_cnybtc')
socket.emit('subscribe', 'marketdata_cnyltc')
socket.emit('subscribe', 'marketdata_btcltc')
socket.emit('subscribe', 'grouporder_cnybtc')
socket.emit('subscribe', 'grouporder_cnyltc')
socket.emit('subscribe', 'grouporder_btcltc')

payload = get_postdata()
arg = [json.dumps(payload), get_sign(payload)]
socket.emit('private', arg)

instance_prices = Prices()

@socket.on('message')
def message(data):
    pass
    # print("New Message - %s" % data)


@socket.on('trade')
def trade(data):
    print("New Trade - %s" % data)
    collector.collect_trade(data, instance_prices)


@socket.on('ticker')
def ticker(data):
    pass
    # print("New Ticker - %s" % data)


@socket.on('grouporder')
def grouporder(data):
    pass
    # print("New GroupOrder - %s" % data)


@socket.on('order')
def order(data):
    pass
    # print("New Order - %s" % data)


@socket.on('account_info')
def account_info(data):
    pass
    # print("New Account_info - %s" % data)

while True:
    raw_input()