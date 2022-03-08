
prod = "p104, maaza, baverage, 1.5 ltr bootle, 85.00"
print(f"prod :{prod}")
print(type(prod))

print("split".center(40, "-"))
# coverting the string into a list
prd_lst = prod.split(", ")
print(f"prd_lst :{prd_lst}")
print(f"prd_lst[1] :{prd_lst[1]}")
print(f"prd_lst[4] :{prd_lst[4]}")

print("join".center(40, "-"))
# converting a list into a string
print(f"prd_lst :{prd_lst}")
print(type(prd_lst))
prod_res = ", ".join(prd_lst)
print(f"prod_res :{prod_res}")
print(type(prod_res))

print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
tran_table = st.maketrans(a, b)
print(f"trans_table :{tran_table}")

print("translate".center(40, "-"))
trans_res = st.translate(tran_table)
print(f"trans_res :{trans_res}")

print("find".center(40, "-"))
st = "hello world"
print(st.find("l"))
print(st.find("l", 4))

print("replace".center(40, "-"))
st = "hello world"
res = st.replace("h", "H")
res = res.replace("w", "W")
print(f"res :{res}")

print("strip".center(40, "-"))
st = '******hello*********'
print(f"st :{st}")
lres = st.lstrip("*")
print(f"lres :{lres}")
rres = lres.strip("*")
print(f"rres :{rres}")

res= st.strip("*")
print(f"res :{res}")

