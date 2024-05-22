import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class BookDAO:
    def __init__(self):
        # Khởi tạo kết nối đến Firebase Realtime Database
        cred = credentials.Certificate("ServiceAccount.json")
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://btl-python-de2-default-rtdb.firebaseio.com/'})
        self.ref = db.reference('books')

    def create(self, book_data):
        # Tạo một nút mới trong Realtime Database với dữ liệu của sách mới
        new_book = self.ref.push()
        new_book.set(book_data)
        return new_book.key

    def read(self, book_id):
        # Đọc dữ liệu của một sách từ Realtime Database
        book_data = self.ref.child(book_id).get()
        return book_data
    

    def update(self, book_id, new_data):
        # Cập nhật dữ liệu của một sách trong Realtime Database
        self.ref.child(book_id).update(new_data)

    def delete(self, book_id):
        # Xóa một sách khỏi Realtime Database
        self.ref.child(book_id).delete()

class Book:
    def __init__(self, id, title, author, genres, price, images):
        self.id = id
        self.title = title
        self.author = author
        self.genres = genres
        self.price = price
        self.images = images

# Sử dụng BookDAO
book_dao = BookDAO()

# Tạo một sách mới
new_book = {
    "title": "New Book",
    "author": "Author",
    "genres": "Genre",
    "price": 100,
    "images": "image.jpg"
}
new_book_id = book_dao.create(new_book)
print("Created new book with ID:", new_book_id)

# Đọc thông tin của một sách
book_id_to_read = new_book_id
read_book = book_dao.read(book_id_to_read)
print("Read book with ID:", book_id_to_read)
print("Book details:", read_book)

# Cập nhật thông tin của một sách
book_id_to_update = new_book_id
updated_data = {"price": 150}
book_dao.update(book_id_to_update, updated_data)
print("Updated book with ID:", book_id_to_update)

# Xóa một sách
book_id_to_delete = new_book_id
book_dao.delete(book_id_to_delete)
print("Deleted book with ID:", book_id_to_delete)
