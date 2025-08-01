import sqlite3

con = sqlite3.connect('menu.db')

with con:
    con.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            compound TEXT NOT NULL,
            price INTEGER NOT NULL
        );
    ''')

sql = 'INSERT INTO menu (id, name, compound, price) VALUES (?, ?, ?, ?);'

menu = [
    ("Борщ", "Суп из свеклы, капусты и мяса", 250),
    ("Цезарь", "Салат с курицей, сухариками и соусом", 320),
    ("Пельмени", "Традиционные русские пельмени с мясом", 300),
    ("Оливье", "Классический салат с овощами и колбасой", 200),
    ("Шашлык", "Маринованное мясо, жаренное на углях", 400)
]

with con:
    for item in menu:
        con.execute(sql, (None, item[0], item[1], item[2]))