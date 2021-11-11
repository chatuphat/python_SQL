#-----------Create Connection------------------
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
 database="invoice_database"
)
mycursor = mydb.cursor()

#---------Creating a Table -------------------------------
mycursor.execute("CREATE TABLE invitem  \
             (itemNo VARCHAR(255) PRIMARY KEY, \
             groupNo VARCHAR(255) \
             )")

mycursor.execute("CREATE TABLE invwh  \
             (refID VARCHAR(255) PRIMARY KEY , \
             warehouse VARCHAR(255) \
             )")

mycursor.execute("CREATE TABLE invstocktrans  \
             (itemNo VARCHAR(255) , \
             qty int, \
             refId VARCHAR(255), \
             FOREIGN KEY(itemNo) REFERENCES invitem(itemNo), \
             FOREIGN KEY(refID) REFERENCES invwh(refID) \
             )")



# #------Insert Into Table ----------------
sql = "INSERT INTO invitem  (ItemNo, groupNo) VALUES (%s, %s)"
val = [
 ('A001', 'A'),
 ('A002', 'A'),
 ('A003', 'A'),
 ('B001', 'B'),
 ('B002', 'B'),
 ('C001', 'C')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")


sql = "INSERT INTO invwh (refID, warehouse) VALUES (%s, %s)"
val = [
 ('Ref_001', 'RM'),
 ('Ref_002', 'FG'),
 ('Ref_003', 'FG'),
 ('Ref_004', 'RM'),
 ('Ref_005', 'RM'),
 ('Ref_006', 'RM'),
 ('Ref_007', 'FG'),
 ('Ref_008', 'RM'),
 ('Ref_009', 'RM')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")


sql = "INSERT INTO invstocktrans (itemNo,qty,refId) VALUES (%s, %s, %s)"
val = [
 ('A002','2','Ref_001'),
 ('A002','3','Ref_002'),
 ('A002','-1','Ref_002'),
 ('B001','1', 'Ref_006'),
 ('B002','2', 'Ref_007'),
 ('B002','2','Ref_008'),
 ('C001','1','Ref_009')
 
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")


sql = "CREATE VIEW resultData AS SELECT invitem.groupNo , invstocktrans.qty FROM invitem INNER JOIN invstocktrans ON invitem.itemNo = invstocktrans.itemNo WHERE qty >=1;"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



mycursor.execute("SELECT groupNo, COUNT(groupNo) FROM resultData GROUP BY groupNo")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  