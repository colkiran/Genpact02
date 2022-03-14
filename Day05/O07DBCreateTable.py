
import  pymysql

conn = pymysql.connect(host="localhost", user='root', password="", port=3306, database='products')

cur = conn.cursor()

query = """
create table products (
prodid varchar(6) PRIMARY KEY,
prodname varchar(50) NOT NULL,
category varchar(50) NOT NULL,
price float NOT NULL,
qty int NOT NULL
)
"""

cur.execute(query)

conn.commit()
conn.close()

