# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price 
        self.__secret = "This is a secret" # Will show error if we access it outside the class

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price*self._discount)
        else: 
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount  # _ means this attribute should only be used inside the class



# TODO: create some book instances
b1 = Book("War and Peace", "Author 1" ,1225,50)
b2 = Book("The Catcher in the Rye","Author 2",123,20)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2.__secret) # This will print an error
print(b2._Book__secret) # This can print