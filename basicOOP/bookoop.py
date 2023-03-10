

# class Book:
#     def __init__(self, title, quantity, author, price):
#         self.title = title
#         self.quantity = quantity
#         self.author = author
#         self.price = price

# book1 = Book('Book 1', 12, 'Author 1', 120)
# book2 = Book('Book 2', 18, 'Author 2', 220)
# book3 = Book('Book 3', 28, 'Author 3', 320)

# print(book1)
# print(book2)
# print(book3)

# The code above will print out 
#<__main__.Book object at 0x00000156EE59A9D0>
#<__main__.Book object at 0x00000156EE59A8B0>
#<__main__.Book object at 0x00000156EE59ADF0>

# This is due to the class and memory location of the objects being printed 


class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    #Using the __repr__ . The self.title and so on are referenced
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)
book3 = Book('Book 3', 28, 'Author 3', 320)

print(book1)
print(book2)
print(book3)
