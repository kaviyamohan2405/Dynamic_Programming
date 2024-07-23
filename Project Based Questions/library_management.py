import streamlit as st
from datetime import datetime, timedelta

# Data storage
books = {}
members = {}

class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True
        self.due_date = None

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []
        self.borrowing_history = []

# Functions to manage books and members
def add_book(book_id, title, author, genre):
    books[book_id] = Book(book_id, title, author, genre)

def update_book(book_id, title=None, author=None, genre=None):
    book = books.get(book_id)
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if genre:
            book.genre = genre

def remove_book(book_id):
    if book_id in books:
        del books[book_id]

def register_member(member_id, name):
    members[member_id] = Member(member_id, name)

def borrow_book(member_id, book_id):
    member = members.get(member_id)
    book = books.get(book_id)
    
    if not member or not book:
        return "Member or Book not found"

    if len(member.borrowed_books) >= 5:
        return "Borrowing limit reached"

    if not book.available:
        return "Book not available"

    book.available = False
    book.due_date = datetime.now() + timedelta(days=30)
    member.borrowed_books.append(book_id)
    member.borrowing_history.append((book_id, 'Borrowed', datetime.now()))

def return_book(member_id, book_id):
    member = members.get(member_id)
    book = books.get(book_id)
    
    if not member or not book:
        return "Member or Book not found"

    if book_id not in member.borrowed_books:
        return "Book was not borrowed by this member"

    book.available = True
    book.due_date = None
    member.borrowed_books.remove(book_id)
    member.borrowing_history.append((book_id, 'Returned', datetime.now()))

def search_books(query):
    result = []
    for book in books.values():
        if (query.lower() in book.title.lower() or
            query.lower() in book.author.lower() or
            query.lower() in book.genre.lower()):
            result.append(book)
    return result

# Streamlit app
def main():
    st.title("Library Management System")

    menu = ["Manage Books", "Manage Members", "Borrow/Return Books", "Search Books"]
    choice = st.sidebar.selectbox("Select Activity", menu)

    if choice == "Manage Books":
        st.subheader("Add / Update / Remove Books")

        book_id = st.text_input("Book ID")
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")

        if st.button("Add Book"):
            add_book(book_id, title, author, genre)
            st.success(f"Book '{title}' added successfully!")

        if st.button("Update Book"):
            update_book(book_id, title, author, genre)
            st.success(f"Book '{book_id}' updated successfully!")

        if st.button("Remove Book"):
            remove_book(book_id)
            st.success(f"Book '{book_id}' removed successfully!")

    elif choice == "Manage Members":
        st.subheader("Register New Member")

        member_id = st.text_input("Member ID")
        name = st.text_input("Name")

        if st.button("Register Member"):
            register_member(member_id, name)
            st.success(f"Member '{name}' registered successfully!")

    elif choice == "Borrow/Return Books":
        st.subheader("Borrow / Return Books")

        member_id = st.text_input("Member ID")
        book_id = st.text_input("Book ID")

        if st.button("Borrow Book"):
            result = borrow_book(member_id, book_id)
            if result:
                st.error(result)
            else:
                st.success(f"Book '{book_id}' borrowed successfully!")

        if st.button("Return Book"):
            result = return_book(member_id, book_id)
            if result:
                st.error(result)
            else:
                st.success(f"Book '{book_id}' returned successfully!")

    elif choice == "Search Books":
        st.subheader("Search Books")

        query = st.text_input("Search by Title, Author, or Genre")

        if st.button("Search"):
            results = search_books(query)
            if results:
                st.write("Books Found:")
                for book in results:
                    st.write(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Genre: {book.genre}, Available: {book.available}")
            else:
                st.write("No books found.")

if __name__ == "__main__":
    main()
