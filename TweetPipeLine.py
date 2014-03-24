from TwitterAPI import TwitterAPI 
import sqlite3

api = TwitterAPI('CsMWX8vAweukXhwNN30PA','FGjpr2Eq8FhPH4xSOFcmpuWe1zu64L0cPwq9cMW2g','38853704-PtmuZbtLAmKHi5pLNUiwIoFrzIQZH87St0A2cmNyu','Go8sFqXQOzC4EG5vDGB9EONDJsd0WNIp4cQU3lPAvQXV9')
# BB codes (SWLONG,SWLAT,NELONG,NELAT):
# Nederland = '3.2,50.7,7.3,53.7'

connection = sqlite3.connect('nssdb.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tweets
             (user text, userid text, content text, coor text, time text, tweetid text)''')

r = api.request('statuses/filter', {'track':'nss, nuclear security summit, nuclear'})
print r.response
x = 0
for item in r.get_iterator():
	if item['coordinates']:
		tweetTuple=(item['user']['screen_name'], item['user']['id_str'], item['text'], str(item['coordinates'][u'coordinates']), item['created_at'], item['id_str'])
	else:
		tweetTuple=(item['user']['screen_name'], item['user']['id_str'], item['text'], item['coordinates'], item['created_at'], item['id_str'])
	print tweetTuple
	cursor.execute('INSERT INTO tweets VALUES (?,?,?,?,?,?)', tweetTuple)
	connection.commit()


	