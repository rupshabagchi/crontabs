
'''
Blocks websites by redirecting them to the localhost. 
Checks if the current time lies between the range of times specified by the user.
'''

import time
from datetime import datetime as dt 


hosts_path=r"\etc\hosts" 
redirect="127.0.0.1"
website_list=["www.facebook.com","kissanime.io","www.twitter.com"]

while(1):
    #Customize according to needs
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,11):
         print("Site blocked")
         with open(hosts_path,'r+') as file:
             content=file.read()               
             for website in website_list:
                 if website in content:
                     pass                        
                 else:
                     file.write(redirect+"  " +website+ "\n")

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Not blocked at this time.")
time.sleep(5)
