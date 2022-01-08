import sqlite3

con = sqlite3.connect("myDatabase.db")

cursorObj = con.cursor()

cursorObj.execute(
    "CREATE TABLE Student (rollno integer primary key, name text, department text)")

cursorObj.execute(
    "insert into Student(rollno, name, department) values(12,'Satyam Singh', 'BCA')")
cursorObj.execute(
    "insert into Student(rollno, name, department) values(13,'Arushi Singh', 'BCA')")
cursorObj.execute(
    "insert into Student(rollno, name, department) values(14,'Ajay Deshmukh', 'BCA')")
cursorObj.execute(
    "insert into Student(rollno, name, department) values(15,'Shivani Rao', 'BCA')")

cursorObj.execute("SELECT * FROM Student")

rows = cursorObj.fetchall()
print(rows)
con.commit()

print("Id", "    ", "Name ", "       ", "Department")
print("-------------------------------------------")
for row in rows:
    print(row[0], "    ", row[1], "     ", row[2])

cursorObj.execute("drop table Student")
con.close()
