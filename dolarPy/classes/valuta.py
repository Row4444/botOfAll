import requests
import datetime
import json

from consts import*
from date import getSomeDay






def dollar(date = 0):
    inDay = getSomeDay(date) 
    req = requests.get(URL + inDay)
    return req.json()['exchangeRate'][CURRENCY['dollar']]['saleRateNB']


def euro(date = 0):
    inDay = getSomeDay(date) 
    req = requests.get(URL + inDay)
    return req.json()['exchangeRate'][CURRENCY['euro']]['saleRateNB']


def ruble(date = 0):
    inDay = getSomeDay(date) 
    req = requests.get(URL + inDay)
    return req.json()['exchangeRate'][CURRENCY['ruble']]['saleRateNB']

print(dollar())
print(euro())
print(ruble())







