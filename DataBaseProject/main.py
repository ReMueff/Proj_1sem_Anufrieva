from sqlite3 import *

table = [[1,'Алексей', 1, 22, 1000], [2, 'Миша', 1, 19, 800], [3, 'Сергей', 1, 19, 900],
         [4, 'Мария', 2, 18, 1500], [5, 'Александр', 1, 20, 1100]]

with connect('saper.db') as con:
    cur = con.cursor()
#     cur.executemany("INSERT INTO NewTable VALUES (?, ?, ?, ?, ?)", table)
    print(cur.execute("SELECT * FROM NewTable").fetchall())
    print(cur.execute("SELECT * FROM NewTable WHERE sex=2").fetchall())
    print(cur.execute("SELECT * FROM NewTable WHERE score<1000").fetchall())
    print(cur.execute("SELECT * FROM NewTable WHERE old BETWEEN 18 AND 20").fetchall())
    cur.execute("UPDATE NewTable SET old=19 WHERE old=19")
    cur.execute("UPDATE NewTable SET score=score+300 WHERE score<1000")
    cur.execute("UPDATE NewTable SET score=score+100 WHERE old=20")
    cur.execute("DELETE FROM NewTable WHERE score<1000")



