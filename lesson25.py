# --------------- encapsulation --------------------

# class Test:

#     x = 10
# x = 7

# print(x)
# print(Test.x)


# class Test:

#     __x = 10

# print(Test.__x)


# class Human:

#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age

#     def set_age(self, new_age):
#         if new_age >= 0:
#             self.__age = new_age
#         else:
#             self.__age = self.__age


#     def info(self):
#         return f'{self.name}, {self.__age}'
    
# user1 = Human('Yura', 15)
# user1.set_age(16)
# # print(Human.__dict__)
# print(user1.info())




# class Human:

#     __age = 18

#     # def __init__(self, age):
#     #     self.__age = age

#     def get_age(self): # public
#         return self.__age # private
    
#     def set_age(self, new_age):
#         if new_age >= 0:
#             self.__age = new_age

#     def del_age(self):
#         del self.__age


# print(Human.__dict__)


# user1 = Human(15)
# user1.set_age(17)
# user1.del_age()
# print(user1.get_age())

# class Human:

#     __age = 18

# print(Human._Human__age)



# class BankAccount:

#     def __init__(self, account_number, balance = 0):
#         self.__account_number = account_number
#         self.__balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         self.__balance += amount
#         self.transactions.append(f'Deposit: +${amount}')

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             self.transactions.append(f'Withdraw: -${amount}')
#         else:
#             print('ERROR')
    
#     def transfer(self, other_account, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#             other_account.__balance += amount
#             self.transactions.append(f'Transfer to {other_account.__account_number}: -${amount}')
#             other_account.transactions.append(f'Transfer from {self.__account_number}: +${amount}')
#         else:
#             print('ERROR')

#     def generate_statement(self):
#         print(self.transactions, self.__balance)

#     def get_balance(self):
#         return self.__balance
    
#     def clear_transactions(self):
#         self.transactions.clear()

# Yura = BankAccount('1111 1234 7856 9654')
# Sergo = BankAccount('1010 0100 1101 7896')
# Yura.deposit(3750)
# Yura.deposit(3500)
# Yura.withdraw(1730)
# Yura.transfer(Sergo, 3000)
# Sergo.deposit(1800)
# Yura.generate_statement()
# Sergo.generate_statement()

import math
# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        if (self.collection) % self.items_per_page == 0:
            return self.collection // self.items_per_page
        else:
            return self.collection // self.items_per_page + 1

    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        else:
            if len(self.collection) % self.items_per_page == 0:
                return self.items_per_page
            else:
                if page_index == self.page_count() - 1:
                    return len(self.collection) % self.items_per_page
                else:
                    return self.items_per_page

    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        return math.ceil(item_index / self.items_per_page) - 1


helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0) # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalids