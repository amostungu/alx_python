#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    cur = db.cursor()
    cur.execute("SELECT * FROM statesWHERE name LIKE BINARY '{}'".format(argv[4]))

    rows = cur.fetchall()
    for j in rows:
        print(j)
    # Clean up process
    cur.close()
    db.close()
