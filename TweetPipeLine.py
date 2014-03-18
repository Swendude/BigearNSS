from TwitterAPI import TwitterAPI 
api = TwitterAPI('CsMWX8vAweukXhwNN30PA','FGjpr2Eq8FhPH4xSOFcmpuWe1zu64L0cPwq9cMW2g','38853704-PtmuZbtLAmKHi5pLNUiwIoFrzIQZH87St0A2cmNyu','Go8sFqXQOzC4EG5vDGB9EONDJsd0WNIp4cQU3lPAvQXV9')
# BB codes (SWLONG,SWLAT,NELONG,NELAT):
# Nederland = '3.2,50.7,7.3,53.7'
r = api.request('statuses/filter', {'track':'nss'})
print r.response
for item in r.get_iterator():
    print "---------------"
    print item[u'text']