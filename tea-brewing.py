#!/usr/bin/env python


import pynotify
import sys
import time
from os import path


def main(argv):
    if len(argv) != 2:
        print "tea brewing time?:"
        print
        print path.basename(argv[0]) + " 5"
        print
        print "(5 minutes)"
        return 1

    if not pynotify.init("Teatime"):
        print "Error!"
        return 1

    try:
        time.sleep(int(argv[1]) * 60)
    except ValueError:
        print "'" + argv[1] + "' Try again."
        return 1

    n = pynotify.Notification("Teatime!", "Time for tea.")

    if not n.show():
        print "Error!"
        return 1


if __name__ == '__main__':
sys.exit(main(sys.argv))
