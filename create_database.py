import sqlite3

connection = sqlite3.connect("online_store.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    country TEXT NOT NULL,
    email TEXT
)
""")

cursor.execute("""
insert INTO customers
(customer_name, country, email)
VALUES
('husni', 'canada', 'ahmed@gmail.com'),
('mahad', 'UK','kuul@gmail.com'),
('asha', 'nairobi', 'xilkas@gmail.com'),
('xilkas', 'china', 'xilkas@gmail.com'),
('changa' ,'canada', 'changa@gmail.com'),
('haider', 'UK', 'haider@gmail.com'),
('asha', 'xilkas', 'xilkas@gmail.com'),
('mumtaaz', 'us', 'mumtaaz@gmail.com'),
('cagaar', 'us', 'cagaar@gmail.com'),
('jareerka', 'germany', 'jareerka@gmail.com'),
('viera','germany', 'viera@gmail.com'),
('ubo', 'ireland', 'ubo@gmail.com'),
('ugaska', 'UAE', 'ugaska@gmail.com'),
('gaadaco', 'UAE', 'gadaco@gmail.com'),
('dholey', 'india', 'dholey@gmail.com'),
('zaki' ,'india', 'zaki@gmail.com'),
('rob', 'saudi', 'rob@gmail.com'),
('deeq', 'rusia', 'deeq@gmail.com'),
('siarji', 'pakistani', 'siraji@gmail.com'),
('frank', 'ghana', 'frank@gmail.com'),
('mike', 'ghana', 'mike@gmail.com');
""")
#CREATE PRODUCT TABE
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    price INTEGER
    
)
""")

cursor.execute("""
INSERT INTO products
(product_name, price)
VALUES
("laptop", 1200),
("mouse", 25),
("keyboard", 70),
("monitor", 350),
("headphones", 120)
""")

# CREATE ORDER TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS ORDERS    (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER ,
    order_date TEXT
    
)
""")

cursor.execute("""
INSERT INTO ORDERS
(order_id,customer_id, order_date)
VALUES
(1, 1,"2026-07-10"),
(2, 2,"2026-07-11"),
(3, 1,"2026-07-12")
""")


#create order items
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items   (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER ,
    product_id INTEGER,
    quantity INTEGER
    
)
""")


cursor.execute("""
INSERT INTO order_items
(order_item_id, order_id, product_id, quantity)
VALUES
(1,1,1,1),
(2,2,1,2),
(3,3,1,1)
""")






connection.commit()
connection.close()