import datetime
import requests
import json

# === Сегодня ===
datetime.datetime.today().strftime('%d.%m.%Y')

# === Вчера ===
def getYesterday(): 
	today=datetime.date.today() 
	oneday=datetime.timedelta(days=1) 
	yesterday=today-oneday  
	return yesterday.strftime('%d.%m.%Y')


a = getYesterday()

r = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date='+ str(a))

b = r.text
print(b)