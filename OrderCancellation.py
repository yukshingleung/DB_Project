from Exit import exit


def cancel(conn):
    cur = conn.cursor()
    print(' — — — cancel Items with a customer — — - \n')
    order_id = input('Enter order id you want to cancel : ')
    sql = 'select oid from orderlist where oid=\'' + order_id + '\''
    # print(sql)
    cur.execute(sql)
    order_id = cur.fetchone()
    # print(order_id[0])
    if len(order_id) == 0:
        print(' The order is not exists')
    else:
        sql = "select * from item where iid=\'" + order_id[2] + '\''
        cur.execute(sql)
        itemList = cur.fetchall()

        if len(itemList) == 0:
            print(" - - - No items match - - - ")
        else:
            print(" - - - Item List of order", order_id, " - - - ")
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
    n = int(input(' Press 1 to cancel item, or press 0: '))
    print('\n')
    if n == 0:
        exit()
    elif n == 1:
        print(' - - -Cancel - - - \n')
        cid = input('Enter costumer id: ')
        iid = input('Enter item id: ')
        sid = order_id[3]
        quantity = order_id[4]
        # 判断order中是否存在此item
        sql_1 = 'select iid from orderlist where cid=\'' + \
            cid + '\' AND sid=\'' + sid + '\''
        cur.execute(sql_1)
        iid_list = [x[0] for x in cur.fetchall()]
        print("List:", iid_list)
        if iid in iid_list:
            sql_2 = 'select qty from item where sid=%s and iid=%s'
            val_2 = (sid, iid)
            cur.execute(sql_2, val_2)
            total_qty = cur.fetchone()
            rest_qty = total_qty[0] + quantity
            if rest_qty >= 0:
                # 更新item数据库对应数据的quantity
                sql_3 = 'update item set qty = %s where sid=%s and iid=%s'
                val_3 = (rest_qty, sid, iid)
                cur.execute(sql_3, val_3)
                conn.commit()
                # 插入orderlist
                sql_4 = 'insert into orderlist (cid, iid, sid, qty) values (%s, %s, %s, %s)'
                val_4 = (cid, iid, sid, quantity)
                cur.execute(sql_4, val_4)
                conn.commit()
                print(" — — — SUCCESS — — — \n")
                exit()
            else:
                print(" fail ")
                exit()
        else:
            print("Item {} is not in {}".format(iid, sid))
            exit()
