# --------------- JSON --------------
# https://Sergey.com
# {
#     "name":"Sergo",
#     "age":7,
#     "uxex":"Nema"
# }

# import json

# json.dump
# json.load

# data = {
#     "name":"Sergo",
#     "age":7,
#     "uxex":"Nema"
# }

# with open('sergo.json', 'w') as file:
#     json.dump(data, file, indent=4)

# with open('sergo.json', 'r') as file:
#     mydict = json.load(file)
# print(mydict)

# ------------------- raise ------------------
# name = input('Enter name:  ')
# if name == 'Sergo':
#     raise Exception('Sergo nema exception')
# else:
#     print(f'{name} normal person')

# set1 = {7, 10, 5, 6, 16, 9, 8, 7}
# print(hash(7))

# x = (i ** 2 for i in range(10))
# print([i ** 2 for i in range(10)])
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())


# def func():
#     yield 10

# print(func().__next__())

# mylist = [7, 4, 5, 6, 3, 2, 1, 10]
# mylist[6] -> 1