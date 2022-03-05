import os
import os.path
from win10toast import ToastNotifier
toaster = ToastNotifier()
import requests
from time import sleep
from datetime import datetime  

if not os.path.isfile("on_or_offline_log.txt"):
    open("on_or_offline_log.txt", "w+")

status = 0

def online(url="http://www.goole.com"):
    url = url
    timeout = 5
    try:
        request = requests. get(url, timeout=timeout)
        return True
    except (requests. ConnectionError, requests. Timeout) as exception:
        return False

while True:
    if True:
        if online() :
            with open("on_or_offline_log.txt", "a") as log:
                log.write("\nOnline " + str(datetime.now()))
                log.close()
            if status == 0:
                status -= status
                status += 1
                toaster.show_toast("Online", "hooray!!!")

        elif not online():
            with open("on_or_offline_log.txt", "a+") as log:
                log.write("\nOffline " + str(datetime.now()))
                log.close()
            if status == 1:
                status -= status
                status += 0
                toaster.show_toast("Offline" ,"Oh no!!!")