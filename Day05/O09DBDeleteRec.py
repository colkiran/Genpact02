
import  pymysql
conn = pymysql.connect(host="localhost", user='root', password="", port=3306, database='products')
cur = conn.cursor()

query = """
delete from products where prodid = 'prd003'
"""

cur.execute(query)
conn.commit()
conn.close()