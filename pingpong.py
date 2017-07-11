"""
Keeps pinging to prevent a heroku dyno from sleeping
"""

import time
import sys
import requests


def main():
    URL = 'My Website'

    while True:
        try:
            print('Pinging')
            requests.get(URL)
            time.sleep(60 * 15)
        except KeyboardInterrupt:
            print('\nExiting')
            sys.exit(0)

if __name__ == '__main__':
main()
