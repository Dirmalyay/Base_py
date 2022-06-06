# Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON.
import json
import pickle

computers = [
    {"type": "laptop",
     "mark": "lenovo",
     "price": 300
    },
    {"type": "laptop",
     "mark": "mac",
     "price": 1300
    },
    {"type": "all-in-one",
     "mark": "acer",
     "price": 830
     }
]

with open("computers.pkl", 'wb') as c:
    pickle.dump(computers, c)

with open('computer.json', 'w') as cm:
    json.dump(computers, cm)
