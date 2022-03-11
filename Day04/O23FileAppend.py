
"""
if the file is already existing then, it will not disturb the previous contents and add the
new contents into the file

if the file is not existing then creates new file and adds the contents into the file

"""


FA  = open("myfile.txt", "a")

st = input("Enter the contents of the file :")

FA.write(st + "\n")

FA.close()