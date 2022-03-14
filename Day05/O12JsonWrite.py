
import json

player = {
    'players' : [
        {'id': 'P159', 'Name': 'Sachin Tendulkar', 'sport': 'Cricket', 'age': 49},
        {'id': 'P250', 'Name': 'Lionel Messi', 'sport': 'Foot Ball', 'age': 36},
        {'id': 'P325', 'Name': 'Roger Fedrer', 'sport': 'Tennis', 'age': 37},
        {'id': 'P463', 'Name': 'Micheal Jordan', 'sport': 'Basket Ball', 'age': 52},
        {'id': 'P580', 'Name': 'Mike Tyson', 'sport': 'Boxing', 'age': 57}
    ]
}

print(player)

FW = open("C:\\Training\\PycharmProjects\\Genpact02\\Resource\\players.json", "w")
json.dump(player, FW, indent=4)
FW.close()