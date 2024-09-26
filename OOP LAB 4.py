class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"
book1 = Book("The Exorcist", " William Peter Blatty", 1971)
book2 = Book("The Haunting of Hill House", "Shirley Jackson", 1959)
book3 = Book("To kill a mocking bird","Harper Lee","1960")
print(book1)
print(book2)
print(book3)
