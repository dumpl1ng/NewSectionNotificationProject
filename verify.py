import mysql.connector
from connect_sql import insert

#verify that current section number equals to the section number in the database
def verify_sec_num(course_name,course_sec_num):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="",
	  passwd="",
	  database=""
	)

	mycursor = mydb.cursor()

	sql = "SELECT sec_num FROM courses WHERE course_name = %s"
	val = (course_name,)
	mycursor.execute(sql, val)

	result = mycursor.fetchone()

	if(result is None): insert(course_name,course_sec_num)
	if(course_sec_num != result[0]):
		return True
	return False