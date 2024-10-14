# ----------------------- OOP -----------------------

# class Car:
#     pass

# x = Car()
# y = Car()
# z = Car()
# print(x)

# list1 = [1, 2, 3]
# list2 = [5, 1, 0]
# list3 = [1, 2, 3]


# class Car:

#     model = 'Rolls'
#     year = 2020

#     def drive(self): # classMethod
#         print(...)

# car1 = Car()
# car2 = Car()
# car3 = Car()
# car4 = Car()
# print(Car.drive())
# print(car1.drive())


# class Human:


#     def __init__(self, name, age, profession):
#         self.x = name
#         self.y = age
#         self.z = profession

#     def walk(self):
#         return f'Human Walking and {self.about()}'
    
#     def about(self):
#         return f'My name is {self.x} I am {self.y}, my professon is {self.z}'

# user1 = Human("Yura", 15, "Programmer")
# user2 = Human("Gayane", 20, "Programmer")
# user3 = Human("Davo", 20, "Iravaban")
# user4 = Human("Gor", 27, "IT Teacher")
# print(user1.about(), user1.walk())
# print(user1.walk())
# print(user2.about())
# print(user3.about())
# print(user4.about())
# print(user1.__dict__)


# class Tringle:

#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def P(self) -> int|float:
#         return self.a + self.b + self.c
    
#     def S(self):
#         p = self.P() / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# number1 = int(input('Enter number1:  ')) 
# number2 = int(input('Enter number2:  ')) 
# number3 = int(input('Enter number3:  ')) 

# tringle1 = Tringle(number1, number2, number3)
# print(f"Square of triangle = {tringle1.S()}")

# class Soda:

#     def __init__(self, add=None):
#         self.add = add

#     def show_my_drink(self):
#         if self.add:
#             return f'{self.add} gazirovka'
#         else:
#             return 'Sovorakan gazirovka'

# drink1 = Soda()
# drink2 = Soda('Vodka')
# print(drink1.show_my_drink())
# print(drink2.show_my_drink())


# x = 4
# isinstance(x, int)


# try:
#     print('a' + 5)
# except Exception as ex:
#     print(ex.__class__.__name__)


list1 = [2,3,1,2,4,3]
target = 7
arr = []
for i in range(0, len(list1) + 1):
    for j in range(0, i):
        arr.append(list1[j:i])
arr.sort(key=len)
for i in arr:
    if sum(i) == target:
        print(len(i))
        break