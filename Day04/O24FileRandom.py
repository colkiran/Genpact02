
FL = open("data.txt", "r")

pos = FL.tell()
print(f"pos :{pos}")

print("-" * 40)
pos = FL.seek(100, 0)             # 100 bytes from begning of file
print(f"pos :{pos}")
st = FL.read(50)
pos = FL.tell()
print(f"pos :{pos}")



FL.close()