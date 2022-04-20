# 3.Add shop

from Exit import exit


def addShop(conn):
    print(' — — — Add Shop — — - \n')
    while(1):
        # create an instance of the database
        cur = conn.cursor()
        while(1):
            sid = input('Enter shop id: ')
            if sid == "":
                print("please input shop id")
            else:
                break
        sname = input('Enter shop name: ')
        while(1):
            rating = input('Enter shop rating(1-5): ')
            try:
                # 在try里面执行int(rating)判断输入是否为数字
                # 判断rating是否在1-5之间
                if int(rating) < 1 or int(rating) > 5:
                    print("please enter rating in (1-5)")
                else:
                    break
            except:
                print("please enter integer (1-5)")
        location = input('Enter shop location: ')

        sql = 'insert into shop (sid, sname, rating, location) values (%s, %s, %s, %s)'
        val = (sid, sname, rating, location)
        try:
            cur.execute(sql, val)  # execute sql queries
            conn.commit()  # save the changes that are done on the database

            print(' — — — SUCCESS — — — \n')
            exit()
            break
        except:
            print("The id already exists or wrong id!")

# 4.Get all shops


def getAllShops(conn):
    cur = conn.cursor()
    print(' — — — All Shops — — - \n')
    cur.execute('select * from shop')
    shopList = cur.fetchall()  # fetch the retrieved data and save it
    i = 0
    for shop in shopList:
        i += 1
        print(" — — — Shop: ", shop[0], " — — - ")
        print(" Name: ", shop[1])
        print(" Rating: ", shop[2])
        print(" Locationg: ", shop[3])
        print("\n")

    print(" — — — SUCCESS — — — \n")
    exit()
