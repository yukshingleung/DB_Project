from Exit import exit

# 8. Show all item with a shop


def purchase(conn):
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
    n = int(input(' Press 1 to buy item, or press 0: '))
    print('\n')
    if n == 0:
        exit()
    elif n == 1:
        print(' - - -Purchase - - - \n')
        cid = input('Enter costumer id: ')
        iid = input('Enter item id: ')
        sid = shop_id[0]
        quantity = int(input('Enter quantity: '))
        # 判断shop中是否存在此item
        sql_1 = 'select iid from item where sid=\'' + sid + '\''
        cur.execute(sql_1)
        iid_list = [x[0] for x in cur.fetchall()]
        print("List:", iid_list)
        if iid in iid_list:
            sql_2 = 'select qty from item where sid=%s and iid=%s'
            val_2 = (sid, iid)
            cur.execute(sql_2, val_2)
            total_qty = cur.fetchone()
            rest_qty = total_qty[0] - quantity
            if rest_qty >= 0:
                # 更新item数据库对应数据的quantity
                # sql_3 = 'update item set qty = %s where sid=%s and iid=%s'
                # val_3 = (rest_qty, sid, iid)
                # cur.execute(sql_3, val_3)
                # conn.commit()
                # 插入orderlist
                sql_4 = 'insert into orderlist (cid, iid, sid, qty) values (%s, %s, %s, %s)'
                val_4 = (cid, iid, sid, quantity)
                cur.execute(sql_4, val_4)
                conn.commit()
                print(" — — — SUCCESS — — — \n")
                exit()
            else:
                print(" exceed the largest amount! ")
                exit()
        else:
            print("Item {} is not in {}".format(iid, sid))
            exit()
