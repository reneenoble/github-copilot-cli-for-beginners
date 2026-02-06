import pytest
from books import Book, BookCollection


def test_add_book():
    collection = BookCollection()
    collection.add_book("1984", "George Orwell", 1949)

    assert len(collection.books) == 1
    assert collection.books[0].title == "1984"
    assert collection.books[0].author == "George Orwell"
    assert collection.books[0].year == 1949
    assert collection.books[0].read is False


def test_mark_book_as_read():
    collection = BookCollection()
    collection.add_book("Dune", "Frank Herbert", 1965)

    result = collection.mark_as_read(0)

    assert result is True
    assert collection.books[0].read is True


def test_mark_book_as_read_invalid_index():
    collection = BookCollection()
    result = collection.mark_as_read(0)

    assert result is False


def test_remove_book():
    collection = BookCollection()
    collection.add_book("The Hobbit", "J.R.R. Tolkien", 1937)

    result = collection.remove_book(0)

    assert result is True
    assert len(collection.books) == 0


def test_remove_book_invalid_index():
    collection = BookCollection()
    result = collection.remove_book(0)

    assert result is False


def test_book_defaults_to_unread():
    book = Book("Test", "Author", 2020)
    assert book.read is False
