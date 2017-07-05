
"""
creates a new file with the name as current time
"""

import datetime

filename = datetime.datetime.now()

def create_file():
    with open(str(filename.strftime("%Y-%m-%d-%H-%M")),"w+") as file:
        file.write("")

create_file()
