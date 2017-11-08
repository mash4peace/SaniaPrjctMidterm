import sqlite3 as sql
#Creating Database
def createDB():
    try:
        conn = sql.connect("cookieDB.db")
        conn.execute("CREATE TABLE IF NOT EXISTS cookies(id INTEGER PRIMARY KEY Autoincrement, name TEXT NOT NULL , cost FLOAT  NOT NULL)")
        conn.execute("CREATE TABLE IF NOT EXISTS cart(item_id INTEGER , FOREIGN KEY (item_id)REFERENCES cookies(id) )")
        print("Database and two tables are created!!")
    except sql.OperationalError as err :
        print(err)
        print("Database already exists!!!")
def createCookies(cookie):
    conn = sql.connect("cookieDB.db")
    c = conn.cursor()
    c.execute("INSERT INTO cookies(id, name, cost) VALUES (?,?,?)",(cookie))
    conn.commit()
    conn.close()
#To show cookies on the browser
def createCookieList():
    cookieList = []
    cookieList.append([1,"Seasonal Sensation", 4.30 ])
    cookieList.append([2, "Suger Hill Gang", 6.70])
    cookieList.append([3, "Chocolate Pinky Delights", 3.10])
    cookieList.append([4, "Chocolate Chip Peanust Butter Dream", 9.60])
    for cookie in cookieList:
        createCookies(cookie)

    print("Cookie is added in the table")



def showCookie(type):
    conn = sql.connect("cookieDB.db")
    c = conn.cursor()
    c.execute("Select id, name, cost from cookies WHERE id LIKE ?",(type))
    cookies = list(c.fetchall())
    return cookies


