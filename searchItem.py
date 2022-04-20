# searching test
from Exit import exit


def searchItem(conn):
    cur = conn.cursor()
    print(' — — — Item searching — — - \n')
    sitem = input('Search : ')
    sql = "SELECT i.iname, i.price, i.qty, s.sname, s.location FROM item i INNER JOIN shop s ON i.sid = s.sid WHERE " + \
        "'" + sitem + "'" + " IN (i.iname, i.kw1, i.kw2, i.kw3)"

    cur.execute(sql)
    conn.commit()
    sqlresult = cur.fetchall()

    if len(sqlresult) == 0:
        print(' - - - The search result is empty - - - ')
        cur.close()
        exit()

    print(' - - - Search results - - - \n')
    for items in sqlresult:
        print(" Name: ", items[0])
        print(" Price: ", items[1])
        print(" Number of items: ", items[2])
        print(" The shop name: ", items[3])
        print(" Address: ", items[4])
        print("\n")
    print(" — — — SUCCESS — — — ")
    cur.close()
    exit()
