from Exit import exit


def cancel(conn):
    cur = conn.cursor()
    # Get all order list
    sql = "select oid from orderlist"
    cur.execute(sql)
    orderTuple = cur.fetchall()
    orderTuple_List = []
    # Convert to list type
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

    # sql = 'select oid from orderlist where oid=\'' + orderid + '\''  # 找出想要删除的订单号
    # print(sql)
    # cur.execute(sql)
    # order_id = cur.fetchone()  # 获取对应订单号的oid(元组)
    # if len(order_id) == 0:
    #     print(' The order is not exists')
    # else:

    sql = "select * from orderlist where oid=\'" + orderid + '\''  # 查找订单对应的所有属性
    cur.execute(sql)
    orderlist = cur.fetchall()
    print(" ----- Order List of Item", orderid, " ----- ")

    print(" Order ID : ", orderlist[0][0])
    print(" Customer : ", orderlist[0][1])
    print(" Item : ", orderlist[0][2])
    print(" Shop : ", orderlist[0][3])
    print(" Item Quantity: ", orderlist[0][4])

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
        # 删除orderlist对应数据
        sql = 'delete from orderlist where oid = ' + str(orderlist[0][0])
        cur.execute(sql)
        conn.commit()
        print(" — — — SUCCESS — — — \n")
        exit()
