
import  pymysql
conn = pymysql.connect(host="localhost", user='root', password="", port=3306, database='products')
cur = conn.cursor()

query = """
update products set price = 45 where prodid = 'prd002'
"""

cur.execute(query)
conn.commit()
conn.close()
