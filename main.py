import sqlite3

connection = sqlite3.connect("itstep_C2011.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE marvel (film, TEXT);")
cur.execute("INSERT INTO marvel (number, name) VALUES ('1.', 'Перший месник', '2011');")
connection.commit()
cur.execute("INSERT INTO marvel (number, name) VALUES ('2.', 'Капітан Марвел', '2019');")
connection.commit()
cur.execute("INSERT INTO marvel (number, name) VALUES ('3.', 'Залізна людина', '2008');")
connection.commit()
cur.execute("INSERT INTO marvel (number, name) VALUES ('4.', 'Залізна людина 2', '2010');")
connection.commit()
cur.execute("INSERT INTO marvel (number, name) VALUES ('5.', 'Неймовірний Халк', '2008');")
connection.commit()
cur.execute("INSERT INTO marvel (number, name) VALUES ('6.', 'Тор', '2011');")
connection.commit()
