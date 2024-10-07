# -----------------------------------------------------
# n1 = 0
# n2 = 1
# for i in range(40):
#     print(n1)
#     n1, n2 = n2 ,n1 + n2
# -----------------------------------------------------
# number = input('Enter number:  ')
# summ = 0
# for i in number:
#     summ += int(i)
# print(summ)
# -----------------------------------------------------
# number = int(input('Enter number: '))
# fact = 1
# for i in range(1, number + 1):
#     fact *= i
# print(fact)
# -----------------------------------------------------
# gender = input('Enter gender:  ')
# age = int(input('Enter age: '))
# if gender == 'Male' and 18 <= age < 20:
#     print('True')
# else:
#     print('False')

# -----------------------------------------------------
# for i in range(5, 26, 5):
    # print(f'${i - 0.05} --- %{round(i - 0.05 - (i - 0.05) * 60 / 100, 2)}')
# -----------------------------------------------------
# for i in range(0, 101, 10):
#     print(f'{i}(C) = {i * 9/5 + 32}(F)')
# -----------------------------------------------------
# pi = 3
# a, b, c = 2, 3, 4
# for i in range(0, 16):
#     pi += (4 / (a * b * c)) * (-1) ** i
#     a, b, c = a + 2, b + 2, c + 2
#     print(pi)
# -----------------------------------------------------
# for i in range(0, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
# -----------------------------------------------------
# i = 10
# while i < 100:
#     print('Alen and Yura legends')


# for i in range(1, 7):
#     print(i)


# i = 1
# while i <= 6:
#     print(i)
#     i += 1

# while True:
#     number = int(input('Enter Your number:  '))
#     if number == 0:
#         break



# for i in range(50, 60):
#     if i == 5:
#         print('Ka')
#         break
# else:
#     print('chka')


# if -9:
#     print('Yura legend')


# for i in 'python':
#     for j in range(1, 4):
#         print(i, j)



# summ = 0
# count = 0
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     else:
#         summ += number
#         count += 1
# print(summ / count)



# import random

# for i in range(10):
#     text = ''
#     count_O = 0
#     count_P = 0
#     while True:
#         x = random.choice('OP')
#         text += x
#         if x == 'O':
#             count_O += 1
#             count_P = 0
#         elif x == 'P':
#             count_P += 1
#             count_O = 0
#         if count_O == 3 or count_P == 3:
#             print(text)
#             break




