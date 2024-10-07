# ---------------------------------------------------------------
# Գրքից 134
# mylist = [1, 2, 3, 4]
# newlist = []
# for i in range(0, len(mylist) + 1):
#     for j in range(0, i):
#         newlist.append(mylist[j:i])
# newlist.sort(key=len)
# print(newlist)

# [[1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]


# ---------------------------------------------------------------
# Գրքից 135

# n = int(input('Enter number:  '))
# mylist = [i for i in range(2, n + 1)]
# p = 2
# while p < n:
#     for i in mylist:
#         if i % p == 0 and i != p:
#             mylist.remove(i)
#     p += 1
# print(mylist)

            
# ---------------------------------------------------------------
# Գրքից 119
# small_mean = []
# big_mean = []
# items = []
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         break
#     else:
#         items.append(number)
# mean = sum(items) / len(items)
# for i in items:
#     if i > mean:
#         big_mean.append(i)
#     else:
#         small_mean.append(i)
# print(mean, small_mean, big_mean)

# ---------------------------------------------------------------
# Գրքից 118

# text = 'Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?'.lower()
# for i in text:
#     if i.isdigit():
#         continue
#     elif i.isalpha():
#         continue
#     else:
#         if i == ' ':
#             continue
#         else:
#             text = text.replace(i, '')
# list1 = text.split(' ')
# list2 = text.split(' ')
# print(list1 == list2[::-1])

# ---------------------------------------------------------------
# Գրքից 117
# text = "Contractions include....!: don’t,?, !.isn’t, and ....!@wouldn’t."

# text = text.split(' ')
# for i in range(0, len(text)):
#     while True:
#         if text[i][0].isalpha() and text[i][-1].isalpha():
#             break
#         if not text[i][0].isalpha():
#             text[i] = text[i][1:]
#         if not text[i][-1].isalpha():
#             text[i] = text[i][:-1]
# print(' '.join(text))
# # ---------------------------------------------------------------
# Գրքից 114
# small = []
# zero = []
# big = []
# while True:
#     number = input('Enter number:  ')
#     if number == '':
#         print(small, zero, big)
#         break
#     else:
#         number = int(number)
#         if number < 0:
#             small.append(number)
#         elif number == 0:
#             zero.append(number)
#         else:
#             big.append(number)


# ---------------------------------------------------------------
# mylist = ['flower', 'flow', 'flight']
# fl

# mylist = ['flower', 'flow', 'reflight']
# ' '

# mylist = ['flower', 'flow', 'flight']
# mylist.sort(key=len)
# index = 1
# while index < len(mylist):
#     if mylist[0] == mylist[index][:len(mylist[0])]:
#         index += 1
#     else:
#         mylist[0] = mylist[0][:-1]
# print(mylist[0])

# ---------------------------------------------------------------
# import random

# karter = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# master = ['♥', '♦', '♣', '♠']
# kalod = []
# xaxcoxner = []
# for i in range(1, 5):
#     anun = input(f'Xaxcox {i} gri anund brat jan:  ')
#     xaxcoxner.append(anun)
# for i in master:
#     for j in karter:
#         kalod.append(i + j)
# nor_kalod = []
# while kalod != []:
#     cart = random.choice(kalod)
#     nor_kalod.append(cart)
#     kalod.remove(cart)
# for i in xaxcoxner:
#     print(f'{i} --- {nor_kalod[:8]}')
#     nor_kalod = nor_kalod[8:]
# ---------------------------------------------------------------
# x = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# for i in range(len(x)):
#     if i % 2 != 0:
#         x[i] = x[i][::-1]
# print(x)
# ---------------------------------------------------------------
# grid = [
#     ['m', 'y', 'e'], 
#     ['x', 'a', 'm'], 
#     ['p', 'l', 'e']
# ]
# indexes = [1, 3, 5, 8]
# mylist = []
# for i in grid:
#     mylist.extend(i)
# print(mylist)
# for i in indexes:
#     print(mylist[i - 1], end='')
# ---------------------------------------------------------------
# vector = [1, 1, 0, 1, 1, 1]
# max_count = 0
# count = 0
# for i in vector:
#     if i == 1:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#             count = 0
# print(max_count)

# text = '''She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.'''
# text = text.replace('\n', ' ')
# text = text.split(' ')
# print(len(set(text)))


numbers = [9, 3, 10, 5, 7, 6, 4, 1, 2, 8]
n = 10
test = [i for i in range(1, n + 1)]
numbers.sort()
count = 0
for i in range(len(test)):
    if test[i] == numbers[i]:
        count += 1
    else:
        count -= 1
print(count)