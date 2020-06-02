# Store puthon file where you have the database 
import sqlite3
connection = sqlite3.connect('test.db')
print(connection)
crsr = connection.cursor() 

#SQL Command to delete the table if exsist
crsr.execute("DROP TABLE IF EXISTS emp") 

# SQL command to create a table in the database 
sql_command = """CREATE TABLE emp (  
staff_number INTEGER PRIMARY KEY,  
fname VARCHAR(20),  
lname VARCHAR(30),  
gender CHAR(1),  
joining DATE);"""
  
# execute the statement 
crsr.execute(sql_command) 
  
# SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");"""
crsr.execute(sql_command) 
  
# another SQL command to insert the data in the table 
sql_command = """INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");"""
crsr.execute(sql_command) 

sql_command = """SELECT * FROM emp"""

crsr.execute(sql_command)

result = crsr.fetchall()
 
print(result)
  
# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
connection.commit() 
  
# close the connection 
connection.close() 