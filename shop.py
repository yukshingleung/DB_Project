from Exit import exit
# 3. Add a new shop
#   1) Enter a new shop ID
#   2) Insert a new shop
def addShop(conn):
    print(' — — — Add Shop — — - \n')
    while(1):
        cur = conn.cursor()
        # Enter a shop ID
        while True:
            sid = input('Enter shop id: ')
            # make sure that shop id is not ""
            if sid == "":
                print("please input shop id")
            else:
                break
        sname = input('Enter shop name: ')
        while True:
            rating = input('Enter shop rating(1-5): ')
            try:
                # make sure that rating is an integer in [1-5]
                if int(rating) < 1 or int(rating) > 5:
                    print("please enter rating in (1-5)")
                else:
                    break
            except:
                print("please enter integer (1-5)")
        location = input('Enter shop location: ')
        # Insert a new shop
        sql = 'insert into shop (sid, sname, rating, location) values (%s, %s, %s, %s)'
        val = (sid, sname, rating, location)
        try:
            cur.execute(sql, val)
            conn.commit()
            print(' — — — SUCCESS — — — \n')
            exit()
            break
        except:
            print("The id already exists or wrong id!")

# 4. Get all shops
#   1) Show all shops
def getAllShops(conn):
    cur = conn.cursor()
    print(' — — — All Shops — — - \n')
    # Show all shops
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
