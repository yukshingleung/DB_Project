from numpy import double
from Exit import exit

# 8. Show all item with shop name
def ShowAllItemWithShop(conn):
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
    while True:
        shop_id = input('Enter Shop ID: ')
        if shop_id in shopList:
            break
        else:
            print("You enter wrong Shop ID and please enter again! \n")

    sql = "select * from item where sid=\'" + shop_id + '\''
    cur.execute(sql)
    itemList = cur.fetchall()

    if len(itemList) == 0:
        print(" - - - No items available - - - ")
    else:
        print(" - - - Item List of Shop", shop_id, " - - - ")
        for item in itemList:
            print("\n - - - Item ", item[0], " - - - ")
            print(" Item Name:  ", item[1])
            print(" Item Price: ", item[2])
            print(" Key Word 1: ", item[3])
            print(" Key Word 2: ", item[4])
            print(" Key Word 3: ", item[5])
            print(" Quantity:   ", item[6])

    print("\n — — — SUCCESS — — — \n")
    exit()

# 9. Add a new item to a shop
def AddNewItemToShop(conn):
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

    print('\n — — — Add a new Items into a Shop — — - \n')
    while True:
        shop_id = input('Enter Shop ID: ')
        if shop_id in shopList:
            break
        else:
            print("You enter wrong Shop ID and please enter again! \n")

    sql = "select iid from item where sid=\'" + shop_id + '\''
    cur.execute(sql)
    iidTuple = cur.fetchall()
    iidList = []
    for item in iidTuple:
        iidList.append(item[0])

    while True:
        input_iid = input('Enter item id in I# format: ')
        try:
            if input_iid == '' or input_iid == ' ':
                print("Please do not enter empty string.")
            elif input_iid in iidList:
                print("You enter exist Item ID and please enter again! \n")
            else:
                break
        except:
            print("Please do not enter wrong ID.")

    name = input('Enter item name: ')

    while(1):
        price = input('Enter item price(>0): ')
        try:
            if double(price) <= 0:
                print("Please enter price larger than 0")
            else:
                break
        except:
            print("Please enter price larger than 0")

    kw1 = input('Enter kew word 1: (if key word is NULL please enter NULL)')
    kw2 = input('Enter kew word 2: (if key word is NULL please enter NULL)')
    kw3 = input('Enter kew word 3: (if key word is NULL please enter NULL)')
    while(1):
        qty = input('Enter item quantity(>0): ')
        try:
            if int(qty) <= 0:
                print("Please enter quantity larger than 0")
            else:
                break
        except:
            print("Please enter quantity larger than 0")

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
    val = (input_iid, name, price, qty, shop_id)
    cur.execute(sql, val)
    conn.commit()

    print(" — — — SUCCESS — — — \n")
    exit()
