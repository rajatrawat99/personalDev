import time
from datetime import datetime as dt

temphost="hosts1"
hostPath=r"C:\Windows\System32\drivers\etc\hosts" # r helps in removing \n or \T
redirect="127.0.0.1"
websiteList=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,13) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("working hours...")
        with open(temphost,'r+') as file: # opens the file
            content=file.read();
            # print(content) # for testing purpose
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        with open(temphost,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(2)
