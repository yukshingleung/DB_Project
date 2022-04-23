from Exit import exit
import os

# 8. Purchase
#   1) Get oid and set automatically
#   2) Input customer cid
#   3) Purchase cycle
#       3.1) Show shop list and input shop sid
#       3.2) Retrieve item information based on shop id
#       3.3) Input item iid and quantity
#       3.4) Calculate the rest quantity in item table
#       3.5) Check that whether orderlist have same order in this purchase
#       3.6) Insert into order list (insert trigger)
#       3.7) If continue to buy return 3.1), if finish purchase then exit
def purchase(conn):
    cur = conn.cursor()

    # if no record in orderlist, oid = 0; else oid = max(oid) + 1
    sql = 'select max(oid) from orderlist'
    cur.execute(sql)
    order_id = cur.fetchone()
    if order_id[0] == None:
        oid = 0
    else:
        oid = order_id[0] + 1

    print(' - - - Purchase - - - ')
    print("current order id:", oid,"\n")
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

    # Purchase cycle
    while True:
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
            sid = input('Enter Shop ID: ')
            if sid in shopList:
                break
            else:
                print("You enter wrong Shop ID and please enter again! \n")

        # Retrieve item information based on shop id
        sql = "select * from item where sid=\'" + sid + '\''
        cur.execute(sql)
        itemTuple = cur.fetchall()
        itemList = []

        if len(itemTuple) == 0:
            # If no item on this shop
            print(" - - - No items available in Shop", sid, ", and Choose Shop again - - - ")
            continue
        else:
            print(" - - - Item List of Shop", sid, " - - - ")
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

        # Make sure iid in database
        while True:
            iid = input('Enter item id: ')
            if iid in itemList:
                break
            else:
                print("You enter wrong Item ID and please enter again! \n")

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

        # Get quantity of that item
        sql_2 = 'select qty from item where sid=%s and iid=%s'
        val_2 = (sid, iid)
        cur.execute(sql_2, val_2)
        total_qty = cur.fetchone()
        # Calculate the rest quantity
        rest_qty = int(total_qty[0]) - int(quantity)
        if rest_qty >= 0:
            # Check that whether orderlist have same order in this purchase
            sql_3 = "select qty from orderlist where oid=%s and iid=%s and sid=%s"
            val_3 = (oid, iid, sid)
            cur.execute(sql_3, val_3)
            temp = cur.fetchall()
            print("temp", temp)
            conn.commit()
            # if db don't have record (oid, iid, sid)
            if not temp:
                # print("temp is empty")
                # Database have enough quantity
                # update quantity of item with trigger and insert into orderlist
                sql_4 = 'insert into orderlist (oid, cid, iid, sid, qty) values (%s, %s, %s, %s, %s)'
                val_4 = (oid, cid, iid, sid, quantity)
                cur.execute(sql_4, val_4)
                conn.commit()
                print(" — — — SUCCESS — — — \n")
            # if db have same record (oid, iid, sid)
            elif temp:
                print("You already buy same thing, and the quantity will add together.")
                # print("temp is not empty")
                print("temp", temp)
                temp_qty = temp[0][0]
                print("temp_qty", temp_qty)
                print("int(qty)", int(quantity))

                # new order qty = input quantity + exist order qty
                new_qty = int(quantity) + temp_qty
                print("new_qty", new_qty)
                sql_5 = 'update orderlist set qty=%s where oid=%s and iid=%s and sid=%s'
                val_5 = (new_qty, oid, iid, sid)
                cur.execute(sql_5, val_5)
                conn.commit()

                # # Update item table with rest qty instead of trigger
                # sql = "update item set qty=%s where iid=%s and sid=%s"
                # val = (rest_qty, iid, sid)
                # cur.execute(sql, val)
                # conn.commit()
                print(" — — — SUCCESS — — — \n")
            else:
                print("[WRONG]temp wrong and Choose Shop again.")
                continue

            while True:
                n = input('Enter 1 to buy more, and 2 to finish this purchase: ')
                try:
                    if int(n) != 1 and int(n) != 2:
                        print("Please enter 1 or 2.")
                    else:
                        break
                except:
                    print("Please enter 1 or 2.")
            print("\n")
            if int(n) == 1:
                pass
            else:
                exit()
                break

        else:
            print("\nExceed current largest amount and choose Shop again.\n")
