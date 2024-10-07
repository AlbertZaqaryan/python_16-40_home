# ----------------------------------------------------------------------------
# while True:
#     char_counts = 0
#     number_counts = 0
#     password = input('Enter password: ')
#     if len(password) < 8:
#         print('Your password is pink enter again: ')
#     else:
#         if password[0].isupper():
#             for i in password:
#                 if i.isdigit():
#                     number_counts += 1
#                 elif i.isalpha():
#                     continue
#                 else:
#                     char_counts += 1
#             if char_counts >= 2 and number_counts >= 2:
#                 print(password, 'Your password is normal black')
#                 break
#             else:
#                 print('Your password is pink enter again: ')

#         else:
#             print('Your password is pink enter again: ')
# ----------------------------------------------------------------------------
# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# for i in range(len(link)):
#     if link[i] == '=':
#         print(link[i+1:])
#         break
# -------
# print(link[link.index('=') + 1:])
# -------
# link = link.split('=')
# print(link[1])
# -------
# link = link.partition('=')
# print(link[2])
# ----------------------------------------------------------------------------
# text = input('Enter text: ').lower()
# print(text == text[::-1])
# ----------------------------------------------------------------------------
# text = input('Enter text ').lower()
# text = text.replace(' ', '')
# print(text == text[::-1])
# ----------------------------------------------------------------------------
# text = 'Sergey like pink color'
# print(list(text))
# ----------------------------------------------------------------------------
# numbers = input('Enter 5 numbers: ')
# mylist = numbers.split(' ')
# for i in mylist:
#     if int(i) % 2 == 0:
#         print(i)
# ----------------------------------------------------------------------------
# mylist = [7, 7, 7, 7, 8, 5, 6, 9, 1, 2, 3, 4, 4, 4, 4, 6, 9, 8]
# for i in mylist:
#     if i % 2 == 0:
#         mylist.remove(i)
# print(mylist)

# for i in range(len(mylist) - 1, -1, -1):
#     if mylist[i] % 2 == 0:
#         mylist.pop(i)
# print(mylist)

# mylist = [7, 7, 7, 7, 8, 5, 6, 9, 1, 2, 3, 4, 4, 4, 4, 6, 9, 8]
# for i in mylist.copy():
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# print(mylist)
# ---------------------------------------------------------------
# import random

# mylist = ['Sergo', 'Alen', 'Yura', 'Vardges', 'Hakob']
# newlist = []
# while mylist != []:
#     randomName = random.choice(mylist)
#     newlist.append(randomName)
#     mylist.remove(randomName)
# for i in range(0, len(newlist) - 1):
#     print(f'{newlist[i]} --- {newlist[i + 1]}')
# print(f'{newlist[-1]} --- {newlist[0]}')
# ---------------------------------------------------------------

# import random

# mylist1 = ['Sergo', 'Alen', 'Yura', 'Vardges', 'Hakob']
# mylist2 = ['Sergo', 'Alen', 'Yura', 'Vardges', 'Hakob']
# final_list = []
# while len(final_list) < 5:
#     user1 = random.choice(mylist1)
#     user2 = random.choice(mylist2)
#     if user1 == user2:
#         continue
#     else:
#         final_list.append(f'{user1} - {user2}')
#         mylist1.remove(user1)
#         mylist2.remove(user2)
#     if len(mylist1) == 1 and mylist1 == mylist2:
#         mylist1 = ['Sergo', 'Alen', 'Yura', 'Vardges', 'Hakob']
#         mylist2 = ['Sergo', 'Alen', 'Yura', 'Vardges', 'Hakob']
#         final_list = []
# for i in final_list:
#     print(i)
# ---------------------------------------------------------------
# mylist = []

# while True:
#     text = input('Enter text:  ')
#     if text == '':
#         break
#     else:
#         if text not in mylist:
#             mylist.append(text)
# print(mylist)
# ---------------------------------------------------------------
# for number in range(1, 10000):
#     summ = 0
#     for i in range(1, number // 2 + 1):
#         if number % i == 0:
#             summ += i
#     if summ == number:
#         print(number)
# ---------------------------------------------------------------


# ------------------------ ՏՆԱՅԻՆՆԵՐ ---------------------------------

# print([i + j for i in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] for j in ['♥', '♦', '♣', '♠']])
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# master = ['♥', '♦', '♣', '♠']
# kalod = []
# for i in master:
#     for j in karter:
#         kalod.append(i + j)
# print(kalod)
# ---------------------------------------------------------------
# Գրքից 134
# mylist = [1, 2, 3, 4]
# [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]
# ---------------------------------------------------------------
# Գրքից 135

# ---------------------------------------------------------------
# Գրքից 119

# ---------------------------------------------------------------
# Գրքից 118

# ---------------------------------------------------------------
# Գրքից 117

# ---------------------------------------------------------------
# Գրքից 114

# ---------------------------------------------------------------
# mylist = ['flower', 'flow', 'flight']
# fl

# mylist = ['flower', 'flow', 'reflight']
# ' '
# ---------------------------------------------------------------



