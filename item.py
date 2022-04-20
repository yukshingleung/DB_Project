from numpy import double
from Exit import exit

# 8. Show all item with a shop
def ShowAllItemWithShop(conn):
    cur = conn.cursor()
    print(' — — — Get All Items with a Shop — — - \n')
    
    shop_name = input('Enter Shop Name: ')
    sql = 'select sid from shop where sname=\'' + shop_name + '\''
    # print(sql)
    cur.execute(sql)
    shop_id = cur.fetchone()
    # print(shop_id[0])
    if len(shop_id) == 0:
        print(' The shop name is not exists')
    else:
        sql = "select * from item where sid=\'" + shop_id[0] + '\''
        cur.execute(sql)
        itemList = cur.fetchall()

        if len(itemList) == 0:
            print(" - - - No items available - - - ")
        else:
            print(" - - - Item List of Shop", shop_name, " - - - ")
            for item in itemList:
                print(" - - - Item ", item[0], " - - - ")
                print(" Item Name: ", item[1])
                print(" Item Price: ", item[2])
                print(" Item Key Word 1: ", item[3])
                print(" Item Key Word 2: ", item[4])
                print(" Item Key Word 3: ", item[5])
                # print(type(item[5]))
                print(" Item Quantity: ", item[6])
                print("\n")

    print(" — — — SUCCESS — — — \n")
    exit()


# 9. Add a new item to a shop
def AddNewItemToShop(conn):
    cur = conn.cursor()
    print(' — — — Add a New Items to a Shop — — - \n')
    shop_name = input('Enter Shop Name You Want to Insert: ')
    sql = 'select sid from shop where sname=\'' + shop_name + '\''
    # print(sql)
    cur.execute(sql)
    shop_id = cur.fetchone()
    # print(shop_id[0])
    if len(shop_id) == 0:
        print(' The shop name is not exists')
    else:
        sql = "select iid from item where sid=\'" + shop_id[0] + '\''
        cur.execute(sql)
        iidList = cur.fetchall()
    # for iid in iidList:
    #     print(iid[0])
    input_iid = input('Enter item id in I# format: ')
    finish_flag = False
    continue_flag = False
    for iid in iidList:
        if iid[0] == input_iid:
            while True:
                print("The iid you input already exist!")
                print(
                    "If you still want to use this iid, the quantity of this item in this shop will increase 1.")
                increase_or_not = input("yes / no ?")
                if increase_or_not == "yes":
                    sql = "select qty from item where iid=%s and sid=%s"
                    val = (iid[0], shop_id[0])
                    cur.execute(sql, val)
                    qty = cur.fetchone()
                    # print(qty[0])
                    # new_qty = qty[0]+1
                    sql = "update item set qty=%s where iid=%s and sid=%s"
                    val = (qty[0]+1, iid[0], shop_id[0])
                    cur.execute(sql, val)
                    conn.commit()  # Not cursor
                    print(" — — — SUCCESS — — — \n")
                    exit()
                elif increase_or_not == "no":
                    print("And the exist iid are: ", end="")
                    for iid_1 in iidList:
                        print(iid_1[0], ' ', end="")
                    input_iid = input(
                        '\nPlease input a new item id again in I# format: ')
                    for iid_1 in iidList:
                        if iid_1[0] == input_iid:
                            continue_flag = True
                            break
                    if continue_flag:
                        continue_flag = False
                        continue
                    finish_flag = False
                    break
            if finish_flag:
                break

    name = input('Enter item name: ')
    price = double(input('Enter item price: '))
    kw1 = input('Enter kew word 1: (if key word is NULL please enter NULL)')
    kw2 = input('Enter kew word 2: (if key word is NULL please enter NULL)')
    kw3 = input('Enter kew word 3: (if key word is NULL please enter NULL)')
    qty = int(input('Enter quantity of item: '))

    if kw1 != "NULL":
        # print(kw1)
        kw1 = "\'" + kw1 + "\'"
    if kw2 != "NULL":
        # print(kw2)
        kw2 = "\'" + kw2 + "\'"
    if kw3 != "NULL":
        # print(kw3)
        kw3 = "\'" + kw3 + "\'"

    sql = "insert into item values (%s, %s, %s, " + \
        kw1 + "," + kw2 + "," + kw3 + ", %s, %s)"
    val = (input_iid, name, price, qty, shop_id[0])
    cur.execute(sql, val)
    conn.commit()

    print(" — — — SUCCESS — — — \n")
    exit()
