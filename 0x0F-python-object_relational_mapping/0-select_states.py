#!/usr/bin/python3
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    dbc = db.cursor()

    dbc.execute("SELECT * FROM `states`")

    [print(state) for state in dbc.fetchall()]
