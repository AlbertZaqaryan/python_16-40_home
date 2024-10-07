# def romanToInt(s: str) -> int:
#     count = 0
#     romans = {
#         'I':1,
#         'V':5,
#         'X':10,
#         'L':50,
#         'C':100,
#         'D':500,
#         'M':1000
#     }
#     mylist = [romans[i] for i in s]
#     i = 1
#     while i < len(mylist):
#         if mylist[i] <= mylist[i - 1]:
#             count += mylist[i - 1]
#             mylist.pop(i - 1)
#         else:
#             temp_count = mylist[i] - mylist[i - 1]
#             count += temp_count
#             mylist.pop(i)
#             mylist.pop(i - 1)
#     if len(mylist) == 1:
#         count += mylist[0]
#     return count

# print(romanToInt('MCMXCIV'))


# strs = ["flower","flow","flight"]
# strs.sort(key=len)
# index = 1
# while index <= len(strs):
#     if strs[0] == strs[index][:len(strs[0])]:
#         index += 1
#     else:
#         strs[0] = strs[0][:-1]


# mylist = [4, 8, 14, 30, 52, 136, 189, 365, 785, 1235, 2030, 3045]
# n = 2030
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if mylist[mid] == n:
#         print(mid)
#         break
#     elif mylist[mid] < n:
#         start = mid + 1
#     else:
#         stop = mid - 1


# mylist = [7, 4, 5, 9, 10, -3, 6, 0]
# for i in range(0, len(mylist)):
#     for j in range(0, len(mylist)):
#         if mylist[i] < mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)

# ----------------------------------------------------
# mydict = {'a':1}
# myset = {1, 2}

# ----------------------------------------------------

# myset = {3, 6, 1, 2, 16, 3, 1, 2}
# print(myset)
# ----------------------------------------------------

# myset = {7, 5, 4, 10, 16, 3, 2, 0}
# print(myset)
# ----------------------------------------------------


# set1 = {1, 2, 3, 4}
# set2 = {4, 7, 0}
# print(not set1.isdisjoint(set2))
# print(set1 & set2) # hatum
# print(set1 | set2) # miavorum
# print(set1 ^ set2) # miavorum - hatum
# ----------------------------------------------------

# print(set1.union(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set1.intersection(set2))
# ----------------------------------------------------
# mylist = [3, 3, 3, 4, 5, 1, 2, 2, 2, 3, 4]
# print(list(set(mylist)))
# ----------------------------------------------------