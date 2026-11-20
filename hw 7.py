import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

connect.commit()

def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    connect.commit()
    print("Товар успешно добавлен!")

def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    for product in products:
        print(product)

def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    connect.commit()
    print("Цена товара обновлена!")

def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    connect.commit()
    print("Товар удалён!")

create_product("Настольная лампа", 1850, 12)
create_product("Термос", 950, 25)
create_product("Рюкзак", 3200, 8)

print("Все товары:")
read_products()

update_product(1, 2100)

print("После обновления:")
read_products()

delete_product(2)

print("После удаления:")
read_products()

connect.close()