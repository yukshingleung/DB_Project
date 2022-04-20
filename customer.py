# 1.Register customer
from Exit import exit


def registerUser(conn):
    # create an instance of the database
    cur = conn.cursor()
    print(' — — — User Registration — — - \n')
    cid = input('Enter customer id: ')
    cname = input('Enter customer name: ')
    tel = input('Enter customer telephone number: ')
    addr = input('Enter customer address: ')

    sql = 'insert into customer (cid, cname, tel, addr) values (%s, %s, %s, %s)'
    val = (cid, cname, tel, addr)
    cur.execute(sql, val)  # execute sql queries
    conn.commit()  # save the changes that are done on the database

    print(' — — — SUCCESS — — — \n')
    exit()

# 2.All Customer


def getAllUsers(conn):
    cur = conn.cursor()
    print(' — — — All Users — — - \n')
    cur.execute('select * from customer')
    cusList = cur.fetchall()  # fetch the retrieved data and save it
    for cus in cusList:
        print(" — — — Customer: ", cus[0], " — — - ")
        print(" Name: ", cus[1])
        print(" Phone number: ", cus[2])
        print(" Address: ", cus[3])
        print("\n")

    print(" — — — SUCCESS — — — \n")
    exit()
