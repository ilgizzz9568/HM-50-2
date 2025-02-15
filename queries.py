TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT
    productid INTEGER
    )
"""


TABLE_registered = """
CREATE TABLE IF NOT EXISTS registered (
id INTEGER PRIMARY KEY AUTOINCREMENT,
productid INTEGER,
productid TEXT,
category TEXT,
infoproduct TEXT
)
"""


INSERT_TABLE_registered ="""
INSERT INTO products_details (productid, category, infoproduct)
SELECT productid, category, infoproduct
FROM fsm_store
WHERE productid IS NOT NULL AND category IS NOT NULL AND infoproduct IS NOT NULL """


DELETE_TABLE_registered = """
DELETE FROM fsm_store 
WHERE productid IN (SELECT productid FROM products_details)"""


