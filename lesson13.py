# number = 1
# n = 5
# fact = 1
# while number < n:
#     fact *= n
#     n -= 1
# print(fact)

# --------------------------------------------------------

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(45))
# --------------------------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
    #  fib(4) + fib(5)
    # fib(2) + fib(3) + fib(3) + fib(4)
    # fib(0) + fib(1) + fib(1) + fib(2) + fib(1) + fib(2) + fib(2) + fib(3)
    # 0 + 1 + 1 + fib(0) + fib(1) + 1 + fib(0) + fib(1) + fib(0) + fib(3)
# print(fib(6))
# --------------------------------------------------------
# def summ(n):

#     if n == '':
#         return 0
#     else:
#         return int(n) + summ(input('Enter number: '))
    
# print(summ(input('Enter number: ')))

# 18 - 10010
# --------------------------------------------------------


# def dec_to_bin(n):
#     if n == 1:
#         return '1'
#     else:
#         return dec_to_bin(n // 2) + str(n % 2)
# print(dec_to_bin(18))

# --------------------------------------------------------
# def encoder(mylist):
#     if mylist == []:
#         return []
#     else:
#         return [mylist[0]] * mylist[1] + encoder(mylist[2:])

# print(encoder(["A", 12, "B", 4, "A", 6, "B", 1]))
# --------------------------------------------------------
# def decoder(mylist, count = 1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], len(mylist)]
#     elif mylist[0] == mylist[1]:
#         return decoder(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + decoder(mylist[1:], count = 1)
# print(decoder(["A", "A", "A", "A", "A", "A", "A", "A", "A","A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B", "B"]))
# --------------------------------------------------------
# def list_(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == int:
#         return [mylist[0]] + list_(mylist[1:])
#     else:
#         return list_(mylist[0]) + list_(mylist[1:])
# print(list_([1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]))
# --------------------------------------------------------
