from Exit import exit
# 1. Add a new customer
#   1) Enter a new customer id
#   2) Insert a new customer
def addCustomer(conn):
    print(' — — —Add Customer  — — - \n')
    while(1):
        cur = conn.cursor()  # create an instance of the database
        # Enter a new customer id
        while True:
            # make sure that id is not ""
            cid = input('Enter customer id: ')
            if cid == "":
                print("please input customer id")
            else:
                break
        cname = input('Enter customer name: ')
        tel = input('Enter customer telephone number: ')
        addr = input('Enter customer address: ')
        # Insert a new customer
        sql = 'insert into customer (cid, cname, tel, addr) values (%s, %s, %s, %s)'
        val = (cid, cname, tel, addr)
        try:
            # make sure that id is not duplicated
            cur.execute(sql, val)  # execute sql queries
            conn.commit()  # save the changes that are done on the database
            print(' — — — SUCCESS — — — \n')
            exit()
            break
        except:
            print("The id already exists or wrong id!")


# 2.Get all customer
#   1) Show all customers
def getAllCustomer(conn):
    cur = conn.cursor()
    print(' — — — All Users — — - \n')
    # Show all customers
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
