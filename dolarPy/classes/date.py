import datetime
import requests


#  === Сегодня ===
#  datetime.datetime.today().strftime('%d.%m.%Y')


def getSomeDay(dayInPast = 0): 
	""" === Кокая-то дата в прошлом === """
	today = datetime.date.today() 
	if dayInPast >= 0:
		oneday = datetime.timedelta(dayInPast)
		someDay = today - oneday  
		return someDay.strftime('%d.%m.%Y')
	return today.strftime('%d.%m.%Y')










