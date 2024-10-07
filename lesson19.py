# ------------------------ book N 181 ------------------------
# def Coins(amount, count):
#     if amount == 0 or count == 0:
#         return amount == count
#     return Coins(amount - 25, count - 1) or Coins(amount - 10, count - 1) or Coins(amount - 5, count - 1) or Coins(amount - 1, count - 1)
# print(Coins(64, 7))

# ------------------------ book N 176 ------------------------
# def Nato(text):
#     phonetic_alphabet = {
#             'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
#             'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
#             'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
#             'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
#             'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
#             'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
#             'Y': 'Yankee', 'Z': 'Zulu'
#         }
#     if text == '':
#         return ''
#     else:
#         return phonetic_alphabet[text[0]].title() + ' ' + Nato(text[1:])
# text = input('Enter text: ').upper()
# print(Nato(text))
# ------------------------ book N 174 ------------------------
# def baj(a, b):
#     if b == 0:
#         return a
#     else:
#         return baj(b, a % b)
# print(baj(18, 32))
# ------------------- def for best person ALEN ------------------------

# def alen_delon():
#     for i in range(1, 10):
#         print('Alen')

# def calculator(a, b):
#     return a + b
# print(calculator(7, 6))
# ----------------------------------------------------------------------
# import math

# def rec(n):
#     if n <= 0 or n % 2 != 0:
#         return False
#     elif n == 1:
#         return True
#     else:
#         return rec(n / 2)
# print(rec(25))



# n = 824883294
# string = ''
# for i in range(1, n + 1, 10):
#     string += str(i)
# print(string.count('1'))

# n = int(input('Enter number: '))
# bin_list = [f'{i:0{n}b}' for i in range(2 ** n)]
# for i in bin_list:
#     print(i)


def isHappy(n: int) -> bool:
    new = 0
    if n == 1:
        return True
    else:
        try:
            g = str(n)
            length = len(g)
            for i in range(length):
                new += int(g[i]) ** 2
            return isHappy(new)
        except:
            return False
print(isHappy(19))