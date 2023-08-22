import MySQLdb
#importing MySQL

db=MySQLdb.connect(host="localhost", port=3306, user="root" password="root", db="hbtn_0e_0_usa" charset="utf8")
cursor = db.cursor()
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
#Execute the query to fetch states and sort by states.id
query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)
# Close the cursor and connection
cursor.close()
db.close()
