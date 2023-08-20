import MySQLdb
#importing MySQL
import sys
#importing sys
db=MySQLdb.connect(host="localhost", port=3306, password="password", database="hbtn_0e_0_usa")
cursor = db.cursor()
#Execute the query to fetch states and sort by states.id
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
# Close the cursor and connection
cursor.close()
db.close()
