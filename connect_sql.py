import mysql.connector


#Connect to mysql server 
def insert(course_name, sec_num):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="",
	  passwd="",
	  database="new_section_notification"
	)

	mycursor = mydb.cursor()

	sql = "INSERT INTO courses (course_name, sec_num) VALUES (%s, %s)"
	val = (course_name, sec_num)
	mycursor.execute(sql, val)

	mydb.commit()