import datetime
import json


#Initialises or loads the ban DATABASE
banDict = {'Cyrus': 0, 'Jigs': 0}
try:
    with open('LairdexDB.txt', 'r') as lairdexDB:
        banDict = json.load(lairdexDB)
except FileNotFoundError:
    with open('LairdexDB.txt', 'w') as lairdexDB:
        json.dump(banDict, lairdexDB)      
    
#Set a ban in motion for Cyrus or Jigs
def setBanTimer(name, banHours):
    now = datetime.datetime.now()
    banDuration = datetime.timedelta(hours=banHours)
    banEnd = now + banDuration
    banDict[name] = banEnd
    with open('LairdexDB.txt', 'w') as lairdexDB:
        json.dump(banDict, lairdexDB)

#Cancels a ban for Cyrus or Jigs
def resetBanTimer(name):
    banDict[name] = 0
    with open('LairdexDB.txt', 'w') as lairdexDB:
        json.dump(banDict, lairdexDB)
