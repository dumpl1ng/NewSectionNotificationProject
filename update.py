import mysql.connector

#update mysql course section number
def update(course_name, sec_num):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="",
	  passwd="",
	  database=""
	)

	mycursor = mydb.cursor()

	sql = "UPDATE courses SET sec_num = %s WHERE course_name = %s"
	val = (int(sec_num),course_name)
	mycursor.execute(sql, val)

	mydb.commit()