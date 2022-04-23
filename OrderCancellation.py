from Exit import exit

# 9. Cancel the Order in orderlist
#   1) Get all order list
#   2) Get all information of that order
#   3) Confirmation of Cancel
#   4) Delete corresponding order (delete trigger)
def cancel(conn):
    cur = conn.cursor()

    # Get all order list
    sql = "select DISTINCT oid from orderlist" # Add DISTINCT keyword and make sure that it only show one oid
    cur.execute(sql)
    orderTuple = cur.fetchall()
    orderTuple_List = []

    # Convert from tuple type to list
    for order in orderTuple:
        orderTuple_List.append(str(order[0]))

    print("order id:", [int(x) for x in orderTuple_List])
    print(' — — — Cancel An Order — — - \n')

    while True:
        orderid = input('Enter order id you want to cancel : ')
        if orderid in orderTuple_List:
            break
        else:
            print("You enter wrong Order ID and please enter again! \n")

    # Get all information of that order
    sql = "select * from orderlist where oid=" + orderid
    cur.execute(sql)

    list = cur.fetchall()
    # Show all item in this order
    for orderlist in list:
        print(" ----- Order List of Item", orderid, " ----- ")
        print(" Order ID : ", orderlist[0])
        print(" Customer : ", orderlist[1])
        print(" Item : ", orderlist[2])
        print(" Shop : ", orderlist[3])
        print(" Item Quantity: ", orderlist[4])

    # Confirmation of Cancel
    while True:
        n = input(' Enter 1 to continue to cancel, or enter 0 to exit: ')
        try:
            if int(n) != 1 and int(n) != 0:
                print("Please do not enter wrong information.")
            else:
                break
        except:
            print("Please enter 1 or 0.")
    print('\n')

    if int(n) == 0:
        exit()
    elif int(n) == 1:
        # Delete corresponding order
        sql = 'delete from orderlist where oid = ' + str(orderlist[0])
        cur.execute(sql)
        conn.commit()
        print(" — — — SUCCESS — — — \n")
        exit()
