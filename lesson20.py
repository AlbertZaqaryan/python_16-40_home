# try:
#     print(10 / 2)
# except:
#     print('Sergo Division Error')
# -------------------------------------------
# try:
#     x = int(input('Enter number1: '))
#     y = int(input('Enter number2: '))
#     print(x / y)
# except ValueError:
#     print('Enter Only numbers')
# except ZeroDivisionError:
#     print('number2 not equal 0')
# finally:
#     print('Good')
# -------------------------------------------

# try:
#     print(10 / 0)
# except:
#     print('Sergo Not Found')

# -------------------------------------------

# myfile = open("C:\\Users\\ASUS\\Desktop\\china_futbol.txt", 'r')
# print(myfile.read())

# myfile.close()
# -------------------------------------------

# myfile = open("fubol.txt", 'r')
# print(myfile.read())

# myfile.close()
# -------------------------------------------


# with open('fubol.txt', 'r') as myfile:
    # x = myfile.read()
    # print(myfile.readline(3))
    # print(myfile.readline(3))
    # print(myfile.readline(3))
    # print(myfile.readline(3))
    # print(myfile.readline(3))
    # print(myfile.readlines())
#     x = myfile.read().split('\n')
# print(x)
# -------------------------------------------


# with open('fubol.txt', 'a') as file:
#     file.write('\nSerg')
# -------------------------------------------

# with open('fubol.txt', 'w') as file:
#     file.write('Barev Yura')
# -------------------------------------------

# def head(filename):

#     try:
#         with open(filename, 'r') as file:
#             for i in range(5):
#                 print(file.readline().replace('\n', ''))
#     except FileNotFoundError:
#         print('No file')

# file_name = input('Enter filename: ')
# head(file_name)
# -------------------------------------------
# def cat(src, dst):
#     try:
#         with open(src, 'r') as file1:
#             x = file1.read()
#         with open(dst, 'w') as file2:
#             file2.write(x)
#     except FileNotFoundError:
#         print('No File')

# cat('fubol.txt', 'msyeSergo.txt')
# -------------------------------------------
# def long_word(filename):
#     try:
#         with open(filename, 'r') as file:
#             x = file.read()
#         x = x.split('\n')
#         x.sort(key=len)
#         print(x[-1])
#     except FileNotFoundError:
#         print('Error')
    
# long_word('fubol.txt')
# -------------------------------------------


# def long_word(filename):
#     try:
#         with open(filename, 'r') as file:
#             x = file.read().replace('\n', ' ')
#         x = x.split(' ')
#         x = {i:x.count(i) for i in x}
#         words = sorted(x, key=x.get)
#         print(words[-1], x[words[-1]])
#     except FileNotFoundError:
#         print('Error')
    
# long_word('fubol.txt')
# -------------------------------------------


# def sum_numbers(filename):

    # summ = 0
    # with open(filename, 'r') as file:
    #     for i in file.read():
    #         if i.isdigit():
    #             summ += int(i)
    # print(summ)

# sum_numbers('fubol.txt')
# -------------------------------------------


# def remove_sharps(filename):

#     with open(filename, 'r') as file:
#         x = file.read().split('\n')
#     for i in x:
#         if i[0] == '#':
#             x.remove(i)
#     print(x)

# remove_sharps('fubol.txt')
# -------------------------------------------
