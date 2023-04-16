#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur.execute("SELECT cities.name FROM cities JOIN states\
                 ON cities.states_id=states.id"\
                 WHERE states.name = sys.argv[4])
    cities = cur.fetchall()
    for city in cities:
        print(', '.join(city[1]))
