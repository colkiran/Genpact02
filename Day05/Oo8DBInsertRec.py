"""
insert into products values ('prd005', 'Dark Choclate', 'Biscut', 35, 120)
insert into products values ('prd004', 'Dairy Milk', 'Choclate', 80, 30)
insert into products values ('prd003', 'Lays', 'Wayfers', 30, 50)
insert into products values ('prd002', 'KitKat', 'Choclate', 40, 150)
insert into products values ('prd001', 'Pepsi', 'Baverage', 120, 300)
"""

import  pymysql
conn = pymysql.connect(host="localhost", user='root', password="", port=3306, database='products')
cur = conn.cursor()

query = """
insert into products values ('prd001', 'Pepsi', 'Baverage', 120, 300)
"""

cur.execute(query)
conn.commit()
conn.close()


