
import json

JFR = open("C:\\Training\\PycharmProjects\\Genpact02\\Resource\\books.json", "r")
jsonFile = json.load(JFR)
# print(jsonFile)
for book in jsonFile['books']:
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 40)
