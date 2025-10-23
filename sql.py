import sqlite3

## connecct to sqllite
connection=sqlite3.connect("student.db")

#create a cursor object to insert record
cursor =connection.cursor()


table_info="""
Create table IF NOT EXISTS STUDENT(
                 NAME VARCHAR(25),
                 CLASS VARCHAR(25),
                 SECTION VARCHAR(25), 
                 MARKS INT
                 );

"""

cursor.execute(table_info)


cursor.execute("INSERT INTO STUDENT VALUES ('Alice', '10', 'A', 85);")
cursor.execute("INSERT INTO STUDENT VALUES ('Bob', '10', 'B', 78);")
cursor.execute("INSERT INTO STUDENT VALUES ('Charlie', '9', 'A', 92);")
cursor.execute("INSERT INTO STUDENT VALUES ('David', '9', 'B', 88);")
cursor.execute("INSERT INTO STUDENT VALUES ('Eve', '8', 'C', 91);")
cursor.execute("INSERT INTO STUDENT VALUES ('Frank', '10', 'A', 73);")
cursor.execute("INSERT INTO STUDENT VALUES ('Grace', '9', 'C', 82);")
cursor.execute("INSERT INTO STUDENT VALUES ('Hannah', '10', 'B', 95);")
cursor.execute("INSERT INTO STUDENT VALUES ('Ian', '8', 'A', 67);")
cursor.execute("INSERT INTO STUDENT VALUES ('Jane', '9', 'B', 89);")
cursor.execute("INSERT INTO STUDENT VALUES ('Kevin', '10', 'C', 84);")
cursor.execute("INSERT INTO STUDENT VALUES ('Lily', '9', 'A', 90);")
cursor.execute("INSERT INTO STUDENT VALUES ('Mike', '10', 'B', 77);")
cursor.execute("INSERT INTO STUDENT VALUES ('Nina', '8', 'C', 80);")
cursor.execute("INSERT INTO STUDENT VALUES ('Oscar', '9', 'A', 75);")
cursor.execute("INSERT INTO STUDENT VALUES ('Paul', '10', 'B', 92);")
cursor.execute("INSERT INTO STUDENT VALUES ('Queen', '9', 'C', 86);")
cursor.execute("INSERT INTO STUDENT VALUES ('Rick', '8', 'A', 79);")
cursor.execute("INSERT INTO STUDENT VALUES ('Sara', '10', 'C', 94);")
cursor.execute("INSERT INTO STUDENT VALUES ('Tom', '9', 'B', 81);")
cursor.execute("INSERT INTO STUDENT VALUES ('Uma', '8', 'A', 76);")
cursor.execute("INSERT INTO STUDENT VALUES ('Victor', '9', 'C', 88);")
cursor.execute("INSERT INTO STUDENT VALUES ('Wendy', '10', 'B', 90);")
cursor.execute("INSERT INTO STUDENT VALUES ('Xavier', '9', 'A', 65);")
cursor.execute("INSERT INTO STUDENT VALUES ('Yara', '10', 'C', 93);")
cursor.execute("INSERT INTO STUDENT VALUES ('Zack', '8', 'B', 72);")
cursor.execute("INSERT INTO STUDENT VALUES ('Aria', '9', 'C', 87);")
cursor.execute("INSERT INTO STUDENT VALUES ('Ben', '10', 'A', 91);")
cursor.execute("INSERT INTO STUDENT VALUES ('Cara', '8', 'B', 74);")
cursor.execute("INSERT INTO STUDENT VALUES ('Dean', '9', 'A', 80);")
cursor.execute("INSERT INTO STUDENT VALUES ('Ella', '10', 'C', 97);")
cursor.execute("INSERT INTO STUDENT VALUES ('Finn', '8', 'A', 68);")
cursor.execute("INSERT INTO STUDENT VALUES ('Gina', '9', 'B', 89);")
cursor.execute("INSERT INTO STUDENT VALUES ('Hugo', '10', 'C', 83);")
cursor.execute("INSERT INTO STUDENT VALUES ('Isla', '8', 'C', 71);")
cursor.execute("INSERT INTO STUDENT VALUES ('Jack', '9', 'A', 90);")
cursor.execute("INSERT INTO STUDENT VALUES ('Kira', '10', 'B', 96);")
cursor.execute("INSERT INTO STUDENT VALUES ('Leo', '8', 'A', 77);")
cursor.execute("INSERT INTO STUDENT VALUES ('Mia', '9', 'C', 82);")
cursor.execute("INSERT INTO STUDENT VALUES ('Noah', '10', 'B', 85);")
cursor.execute("INSERT INTO STUDENT VALUES ('Olive', '8', 'A', 79);")
cursor.execute("INSERT INTO STUDENT VALUES ('Pia', '9', 'B', 88);")
cursor.execute("INSERT INTO STUDENT VALUES ('Quinn', '10', 'C', 92);")
cursor.execute("INSERT INTO STUDENT VALUES ('Rita', '9', 'A', 83);")
cursor.execute("INSERT INTO STUDENT VALUES ('Sam', '8', 'B', 75);")
cursor.execute("INSERT INTO STUDENT VALUES ('Tina', '10', 'C', 89);")
cursor.execute("INSERT INTO STUDENT VALUES ('Umar', '8', 'A', 70);")
cursor.execute("INSERT INTO STUDENT VALUES ('Vera', '9', 'C', 91);")
cursor.execute("INSERT INTO STUDENT VALUES ('Will', '10', 'B', 86);")
cursor.execute("INSERT INTO STUDENT VALUES ('Zoe', '8', 'A', 93);")

# Commit changes
print("The inserted records are")
data=cursor.execute('''select * From STUDENT''')

for row in data:
    print(row)
      
      
  ##close the connections
connection.commit()    
connection.close()