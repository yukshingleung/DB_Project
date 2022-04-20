# 3.Add shop

from Exit import exit


def addShop(conn):
    # create an instance of the database
    cur = conn.cursor()
    print(' — — — Add Shop — — - \n')
    sid = input('Enter shop id: ')
    sname = input('Enter shop name: ')
    rating = input('Enter shop rating: ')
    location = input('Enter shop location: ')

    sql = 'insert into shop (sid, sname, rating, location) values (%s, %s, %s, %s)'
    val = (sid, sname, rating, location)
    cur.execute(sql, val)  # execute sql queries
    conn.commit()  # save the changes that are done on the database

    print(' — — — SUCCESS — — — \n')
    exit()

# 4.Get all shops


def getAllShops(conn):
    cur = conn.cursor()
    print(' — — — All Shops — — - \n')
    cur.execute('select * from shop')
    shopList = cur.fetchall()  # fetch the retrieved data and save it
    i = 0
    for shop in shopList:
        i += 1
        print(" — — — Shop: ", shop[0], " — — - ")
        print(" Name: ", shop[1])
        print(" Rating: ", shop[2])
        print(" Locationg: ", shop[3])
        print("\n")

    print(" — — — SUCCESS — — — \n")
    exit()
