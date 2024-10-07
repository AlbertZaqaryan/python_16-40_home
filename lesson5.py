# -------------------------------------------------------
# cord = input('Enter codinate: ')
# let = cord[0]
# number = int(cord[1])
# if (let in 'aceg' and number % 2 != 0) or (let in 'bdfh' and number % 2 == 0):
#     print('Black')
# else:
#     print('White')
# -------------------------------------------------------
# age = int(input ('enter age'))
# gender = input('enter gender M OR F')
# status = input('enter maritial status Y or N')
# if gender == 'F':
#     print('urban areas')
# elif gender == 'M' and  20 <= age <40:
#     print('work in anywhere')
# elif gender == 'M' and  40 < age <60:
#     print('urban areas only')
# else:
#     print('ERROR')
# -------------------------------------------------------
# m = input('Enter month:  ')
# n = int(input('Enter number:  '))
# if (m == 'March' and 20 <= n <= 31) or (m == ('April' or 'May') and 1 <= n <= 31) or (m == 'June' and 1 <= n < 21):
#     print('Spring')
# elif (m == 'June' and 21 <= n <= 30) or (m == ('July' or 'August') and 1 <= n <= 31) or (m == 'September' and 1 <= n <= 21):
#     print('Summer')
# elif (m == 'September' and 22 <= n <= 30) or (m == ('October' or 'November') and 1 <= n <= 31 ):
#     print('Autumn')
# else:
#     print('Winter')
# -------------------------------------------------------
# for i in range(-14, 30, 5):
#     print(i)
# -------------------------------------------------------

# for i in range(30, -14, -1):
#     print(i)
# -------------------------------------------------------

# for number in range(100):
#     print(number)
# -------------------------------------------------------

# for i in 1234: # int not iterable
#     print(i)
# -------------------------------------------------------


# for i in (10, 11, 12, 13):
#     print(i)
# -------------------------------------------------------


# for i in 10111213:
#     print(i)
# -------------------------------------------------------

# text = 'David Python Developer'
# for i in range(0, len(text)):
#     print(text[i])
# print(text[0])
# print(text[21])
# print(len(text))
# -------------------------------------------------------


# text = 'David Python Developer'
# for i in text:
#     print(i)
# -------------------------------------------------------


# text = 'David Python Developer'
# for i in range(0, len(text)):
#     print(i, text[i])
# -------------------------------------------------------

# text = 'David Python Developer'
# for i in range(len(text) - 1, -1, -1):
#     print(text[i])
# -------------------------------------------------------


# text = 'python'
# 'pyt'
# 'yth'
# 'tho'
# 'hon'
# for i in range(0, len(text) - 2):
#     print(text[i] + text[i + 1] + text[i + 2])
# -------------------------------------------------------

# text = 'hello team'
# print(text[3:5])
# print(text[3:])
# print(text[:4])
# print(text[::-1])
# print(text[0])
# print(text[-1])
# print(text[-1:-4:-1])
# print(text[-4:-1])
# -------------------------------------------------------


# text = 'hello team'
# text = text.split(' ')
# print(text[1] + ' ' + text[0])
# -------------------------------------------------------


# text = 'hello tellllam'
# text = text.replace('l', '$', 3)
# print(text)
# -------------------------------------------------------

# text = 'hello tellllam'
# count = 0
# for i in text:
#     if i == 'l':
#         count += 1
# print(count)
# -------------------------------------------------------

# text = 'python'
# # print(text.index('o'))
# for i in range(0, len(text)): # 0 1 2 3 4 5  p y t h o n
#     if text[i] == 'o':
#         print(i)
# -------------------------------------------------------


# text = 'python'
# for i in text:
#     if i == 'o':
#         break
#     else:
#         print(i)


# text = 'python'
# for i in text:
#     if i == 'o':
#         continue
#     else:
#         print(i)


# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))
# if a > b:
#     for i in range(a, a * b + 1, a):
#         if i % b == 0:
#             print(i)
#             break
# elif b > a:
#     for i in range(b, a * b + 1, b):
#         if i % a == 0:
#             print(i)
#             break
# else:
#     print(a)


# print(ord('A'))
# print(chr(1377))

# print('David' > 'Davo')
# print('Albert' < 'Zaqaryan')


# text = 'David like BMW'
# print(text.count(6, 'i'))


# text = input('Enter text:  ')
# letter_count = 0
# number_count = 0
# char_count = 0
# for i in text:
#     if i.isalpha():
#         letter_count += 1
#     elif i.isdigit():
#         number_count += 1
#     else:
#         char_count += 1
# print(f'Letter count = {letter_count}\nNumber count = {number_count}\nChar count = {char_count}')