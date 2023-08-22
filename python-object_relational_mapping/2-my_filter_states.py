#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches"""
import sys
import MySQLdb

# The code should not be executed when imported
if __name__ == "__main__":
    
    # make a connection to the database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # It gives us the ability to have multiple seperate working environments
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
