#!/usr/bin/python3
"""
A script that  takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
must be safe from SQL injection
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    search = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        if search == state[1]:
            print(state)
