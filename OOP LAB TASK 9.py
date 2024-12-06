class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"

class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    def create(cls, title, author, genre=None, pages=None):
        return cls(title, author, genre, pages)

    def display_info(self):
        base_info = super().display_info()
        genre_info = f", Genre: {self.genre}" if self.genre else ""
        pages_info = f", Pages: {self.pages}" if self.pages else ""
        return base_info + genre_info + pages_info

class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def create(cls, title, author, journal=None, doi=None):
        return cls(title, author, journal, doi)

    def display_info(self):
        base_info = super().display_info()
        journal_info = f", Journal: {self.journal}" if self.journal else ""
        doi_info = f", DOI: {self.doi}" if self.doi else ""
        return base_info + journal_info + doi_info

def save_to_file(filename, documents):
    with open(filename, "w") as file:
        for doc in documents:
            if isinstance(doc, Book):
                file.write(f"Book|{doc.title}|{doc.author}|{doc.genre}|{doc.pages}\n")
            elif isinstance(doc, Article):
                file.write(f"Article|{doc.title}|{doc.author}|{doc.journal}|{doc.doi}\n")

def load_from_file(filename):
    documents = []
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split("|")
                doc_type = data[0]
                if doc_type == "Book":
                    title, author, genre, pages = data[1], data[2], data[3], data[4]
                    documents.append(Book(title, author, genre if genre != "None" else None, int(pages) if pages.isdigit() else None))
                elif doc_type == "Article":
                    title, author, journal, doi = data[1], data[2], data[3], data[4]
                    documents.append(Article(title, author, journal if journal != "None" else None, doi if doi != "None" else None))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Returning an empty list.")
    return documents

if __name__ == "__main__":
    book1 = Book.create("1984", "George Orwell", "Dystopian", 328)
    book2 = Book.create("The Alchemist", "Paulo Coelho")
    article1 = Article.create("AI Ethics", "Jane Doe", "Tech Journal", "10.1000/abc123")
    article2 = Article.create("Quantum Computing Basics", "John Smith")

    print(book1.display_info())
    print(book2.display_info())
    print(article1.display_info())
    print(article2.display_info())

    filename = "documents.txt"
    save_to_file(filename, [book1, book2, article1, article2])
    print(f"Documents saved to {filename}.")

    loaded_docs = load_from_file(filename)
    print("\nLoaded Documents:")
    for doc in loaded_docs:
        print(doc.display_info())
