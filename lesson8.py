# -------------------------------------------------------
# h = int(input('Enter height:  '))
# w = int(input('Enter width:  '))
# for i in range(0, w+1):
#    if i == 0:
#     print('|' + '-' * (w) + '|')
# for j in range(1, h-1):
#     print('|' + ' ' * (w) + '|')
# print('|' + '-' * (w) + '|')
# -------------------------------------------------------
# count = int(input('Enter number count:  '))
# prime_count = 0
# for i in range(count):
#     number = int(input('Enter number:  '))
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             break
#     else:
#         prime_count += 1
# print(prime_count)
# -------------------------------------------------------
# n = int(input('Enter number: '))
# summ = 0
# for i in range(1, n + 1):
#     fact = 1
#     for j in range(1, i + 1):
#         fact *= j
#     summ += fact
# print(summ)
# -------------------------------------------------------
# n = int(input('Enter number count: '))
# max_sum = 0
# max_number = 0
# for i in range(n):
#     number = input('Enter number:  ')
#     summ = 0
#     for i in number:
#         summ += int(i)
#     if summ > max_sum:
#         max_sum = summ
#         max_number = int(number)
# print(max_number)
# -------------------------------------------------------
# mecucun = 4

# for i in range(mecucun):
#     print(' ' * (mecucun - i - 1), end='')
    
#     print('#' * (2 * i + 1))

# -------------------------------------------------------

# mecucun = int(input('Enter number: '))
# number = 1

# for i in range(mecucun):
#     print(' ' * (mecucun - i - 1) * 3, end=' ')  

#     for j in range(i + 1):
#         print(f'{number:2}', end='    ')
#         number += 2

#     print()
# -------------------------------------------------------
# mecucun = 9

# summ = ''
# for i in range(1, mecucun + 1):
#     summ += str(mecucun - i + 1)
#     print(f"{summ}" + '.' * (mecucun * 2 - 2 * i) + f"{summ[::-1]}")
# -------------------------------------------------------
# text = input('Enter text:  ')
# text_s = len(text) * 's'
# while text_s not in text:
#     text_s = text_s[:-1]
# print(len(text_s))
# -------------------------------------------------------
# text = input('Enter text:  ')
# count_s_max = 0
# count_s = 1
# for i in range(0, len(text) - 1):
#     if text[i] == 's' == text[i + 1]:
#         count_s += 1
#         if count_s > count_s_max:
#             count_s_max = count_s
#     else:
#         count_s = 1
# print(count_s_max)
# -------------------------------------------------------
# text = input('Enter text:  ')
# new_text = ''
# for i in range(0, len(text), 2):
#     new_text += text[i]
# for i in range(len(text) - 1, 0, -2):
#     new_text += text[i]
# print(new_text)
# -------------------------------------------------------
# 'p'
# 'py'
# 'pyt'
# 'pyth'
# 'pytho'
# 'python'
# 'pytho'
# 'pyth'
# 'pyt'
# 'py'
# 'p'

# text = input('Enter text:  ')
# for i in range(1, len(text) + 1):
#     print(text[:i])
# for i in range(len(text) - 1, 0, -1):
#     print(text[:i])
# -------------------------------------------------------
s = 1
n = int(input('Enter number: '))
a = 2
for i in range(1, n + 1):
    s += (1 / a) * (-1) ** i
    a *= 2
print(s)