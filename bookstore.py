import sqlite3
MyStore=sqlite3.connect('bookstore.db')
nm=input("Enter Book name:")
sql="SELECT * from stationary WHERE bookname='"+nm+"';"
curstore=MyStore.cursor()
#curstore.execute('''CREATE TABLE stationary ( BookID INTEGER
#PRIMARY KEY AUTOINCREMENT,
#bookname TEXT(20) NOT NULL,
#author TEXT,
#price INTEGER);''')
curstore.execute(sql)
record=curstore.fetchone()
print(record)
#curstore.execute("INSERT INTO stationary(BookID,bookname,author,price) VALUES (2,'PYTHON','Aryabatta',475)")
#curstore.execute("INSERT INTO stationary(BookID,bookname,author,price) VALUES (3,'C#','Elon mask',400)")
#curstore.execute("INSERT INTO stationary(BookID,bookname,author,price) VALUES (4,'C++','Josh buttler',250)")
#curstore.execute("INSERT INTO stationary(BookID,bookname,author,price) VALUES (5,'PERL','Abdul kalam',200)")
MyStore.commit()
MyStore.close()

Cps=int(input("No.of copies:"))
morebooks=input("Add more books:(Y/N)")
if morebooks=="Y":
    print("Enter no.of books:")
elif morebooks=="N":
    print("N")
def Amount():
    print("Total cost:",Cps*475)
Amount()
