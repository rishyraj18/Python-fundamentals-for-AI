class book:
     
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Price :{self.price}")

book1 = book("Atomic Habits", "James Clear", 450)
book1.display()