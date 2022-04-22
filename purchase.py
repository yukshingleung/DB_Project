from Exit import exit

# 8. Purchase
#   1) Show shop list
#   2) Input shop id
#   3) Retrieve item information based on shop id
#   4) Confirmation of purchase
#   5) Input cid, sid, iid and quantity
#   6) Calculate the rest quantity
#   7) Insert into order list (insert trigger)
def purchase(conn):
    cur = conn.cursor()

    # show shop list
    print(" - - - Shop Name List - - - ")
    sql = "select * from shop"
    cur.execute(sql)
    shopTuple = cur.fetchall() # Tuple
    print("SID | ShopName | Rating | Location")
    shopList = []
    for shop in shopTuple:
        shopList.append(shop[0])
        print(shop[0], "|", shop[1], "|", shop[2], "|", shop[3])

    print('\n — — — Get All Items with a Shop — — - \n')
    # Input shop id
    while True:
        shop_id = input('Enter Shop ID: ')
        if shop_id in shopList:
            break
        else:
            print("You enter wrong Shop ID and please enter again! \n")

    # Retrieve item information based on shop id
    sql = "select * from item where sid=\'" + shop_id + '\''
    cur.execute(sql)
    itemTuple = cur.fetchall()
    itemList = []

    if len(itemTuple) == 0:
        # If no item on this shop
        print(" - - - No items available - - - ")
    else:
        print(" - - - Item List of Shop", shop_id, " - - - ")
        for item in itemTuple:
            itemList.append(item[0])
            print("\n - - - Item ", item[0], " - - - ")
            print(" Item Name:  ", item[1])
            print(" Item Price: ", item[2])
            print(" Key Word 1: ", item[3])
            print(" Key Word 2: ", item[4])
            print(" Key Word 3: ", item[5])
            print(" Quantity:   ", item[6])

    print("\n")
    # Confirmation of purchase
    while True:
        n = input('Input 1 to buy item, or input 0 to exit: ')
        try:
            if int(n) != 1 and int(n) != 0:
                print("Please do not enter empty string.")
            else:
                break
        except:
            print("Please enter 1 or 0.")

    print('\n')
    if int(n) == 0:
        exit()
    elif int(n) == 1:
        print(' - - - Purchase - - - \n')
        # Get all cid
        sql = "select cid from customer"
        cur.execute(sql)
        customerTuple = cur.fetchall()
        customerList = []
        # Put cid into list
        for customer in customerTuple:
            customerList.append(customer[0])
        # Make sure cid in database
        while True:
            cid = input('Enter costumer id: ')
            if cid in customerList:
                break
            else:
                print("You enter wrong Customer ID and please enter again! \n")
        # Make sure iid in database
        while True:
            iid = input('Enter item id: ')
            if iid in itemList:
                break
            else:
                print("You enter wrong Item ID and please enter again! \n")
        
        sid = shop_id
        # Make sure quantity larger than 0
        while True:
            quantity = input('Enter quantity(>0): ')
            try:
                if int(quantity) <= 0:
                    print("Please enter quantity larger than 0")
                else:
                    break
            except:
                print("Please enter quantity larger than 0")

        if iid in itemList:
            # Get quantity of that item
            sql_2 = 'select qty from item where sid=%s and iid=%s'
            val_2 = (sid, iid)
            cur.execute(sql_2, val_2)
            total_qty = cur.fetchone()
            # Calculate the rest quantity
            rest_qty = int(total_qty[0]) - int(quantity)
            if rest_qty >= 0:
                # Database have enough quantity
                # update quantity of item with trigger and insert into orderlist
                sql_4 = 'insert into orderlist (cid, iid, sid, qty) values (%s, %s, %s, %s)'
                val_4 = (cid, iid, sid, quantity)
                cur.execute(sql_4, val_4)
                conn.commit()
                print(" — — — SUCCESS — — — \n")
                exit()
            else:
                print(" exceed current largest amount! ")
                exit()
        else:
            print("Item {} is not in {}".format(iid, sid))
            exit()
