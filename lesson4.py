# if 5 < 4: # True
#     print('good')
#     x = 5
#     print(x)

# ---------------------------------------------------
# if elif elif elif elif elif else
# ---------------------------------------------------

# a = int(input('Enter number1: '))
# b = int(input('Enter number2: '))
# if a > b:
#     print('a is max')
# elif b > a:
#     print('b is max')
# else:
#     print('equal')
# ---------------------------------------------------


# a = int(input('Enter number1: '))
# b = int(input('Enter number2: '))

# x = int(input('Enter number1: '))
# y = int(input('Enter number2: '))


# if a > b:
#     print('a is max')
# elif b > a:
#     print('b is max')
# else:
#     print('equal')

# if x > y:
#     print('x is max')
# elif y > x:
#     print('y is max')
# else:
#     print('equal')
# ---------------------------------------------------
# print(type(5) == int)
# print('5'.isdigit())
# print('a'.isalpha())

# ---------------------------------------------------
# let = input('Enter letter: ')
# if let.isdigit():
#     print('Number')
# elif let.isalpha():
#     print('Letter')
# else:
#     print('Symbol')
# ---------------------------------------------------
# let = input('Enter letter: ')
# if let.isupper():
#     print('Mecatar')
# elif let.islower():
#     print('Poqratar')
# else:
#     print('Chka tenc ban')
# ---------------------------------------------------
# dog_age = int(input('Enter dog age:   '))
# if 0 < dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# elif dog_age > 2:
#     print(f'Human age = {4 * (dog_age - 2) + 21}') 
# else:
#     print('Enter valid age')
# ---------------------------------------------------
# let = input('Enter let: ')
# if let in 'aeiou':
#     print('vowel')
# else:
#     print('consonant')
# ---------------------------------------------------
# year = int(input('Enter year: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('Leep')
# else:
#     print('No leep')
# ---------------------------------------------------
# import random
# import time

# name = input('Enter your name:    ')
# start = input('Ready?\n\tYes or No:  ')
# if start == 'Yes':
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print(f'---------------- GOOD {name} STARTING GAME ----------------------')
#     user = int(input(f'{name} enter your number:  '))
#     pc = random.randint(0, 5)
#     user_points = 0
#     pc_points = 0
#     if user == pc: # user = 1 pc = 0
#         user_points += 1
#         print(f'---------------->Win {name}<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#         user = int(input(f'{name} enter your number:  '))
#         pc = random.randint(0, 5)
#         if user == pc: # user = 2 pc = 0 END GAME WIN USER
#             user_points += 1
#             print(f'---------------->Win {name}<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#             print(f'------------------ END GAME WIN {name} --------------------')
#         else: # user = 1 pc = 1
#             pc_points += 1
#             print(f'---------------->Win Pc<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#             user = int(input(f'{name} enter your number:  '))
#             pc = random.randint(0, 5)
#             if user == pc: # user = 2 pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'---------------->Win {name}<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#                 print(f'------------------ END GAME WIN {name} --------------------')
#             else: # user = 1 pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'---------------->Win Pc<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#                 print(f'------------------ END GAME WIN PC --------------------')
#     else:
#         pc_points += 1 # user = 0 pc = 1
#         print(f'---------------->Win Pc<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#         user = int(input(f'{name} enter your number:  '))
#         pc = random.randint(0, 5)
#         if user == pc: # user = 1 pc = 1
#             user_points += 1
#             print(f'---------------->Win {name}<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#             user = int(input(f'{name} enter your number:  '))
#             pc = random.randint(0, 5)
#             if user == pc: # user = 2 pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'---------------->Win {name}<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#                 print(f'------------------ END GAME WIN {name} --------------------')
#             else: # user = 1 pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'---------------->Win Pc<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#                 print(f'------------------ END GAME WIN PC --------------------')

#         else: # user = 0 pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---------------->Win Pc<--------------\n{name} = {user}, pc = {pc}\n{name} points = {user_points}, pc = {pc_points}')
#             print(f'------------------ END GAME WIN PC --------------------')
# else:
#     print('---------------------------- EXIT ------------------------------')
