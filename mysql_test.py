import pymysql
import os
from MainMenu import displayMainMenu
from customer import addCustomer, getAllCustomer
from shop import addShop, getAllShops
from searchItem import searchItem
from item import ShowAllItemWithShop, AddNewItemToShop
from purchase import purchase
from OrderCancellation import cancel


def run():
    conn = pymysql.connect(host='localhost', user='root',
                           passwd='34801708', port=3306, db='shopDB', charset='utf8')

    if os.name == 'posix':
        sys_com = "clear"
    else:
        sys_com = "cls"
    os.system(sys_com)
    displayMainMenu()
    while(1):
        try:
            n = int(input("Enter suitable option: "))
            if n > 10:
                print("Invalid Option")
            else:
                break
        except:
            print("Invalid Option")
    if n == 1:
        os.system(sys_com)
        addCustomer(conn)
    elif n == 2:
        os.system(sys_com)
        getAllCustomer(conn)
    elif n == 3:
        os.system(sys_com)
        addShop(conn)
    elif n == 4:
        os.system(sys_com)
        getAllShops(conn)
    elif n == 5:
        os.system(sys_com)
        searchItem(conn)
    elif n == 6:
        os.system(sys_com)
        ShowAllItemWithShop(conn)
    elif n == 7:
        os.system(sys_com)
        AddNewItemToShop(conn)
    elif n == 8:
        os.system(sys_com)
        purchase(conn)
    elif n == 9:
        os.system(sys_com)
        cancel(conn)
    elif n == 10:
        os.system(sys_com)
        print(" - - - Thank You - - - ")
    # else:
    #     os.system(sys_com)
    #     run()


try:

    if __name__ == "__main__":

        run()


# sql = "select * from shop"
# cur.execute(sql)
# data = cur.fetchall()
# for i in data[:2]:
#     print(i)
# cur.close()
# conn.close()
except pymysql.Error as e:
    print("数据库连接失败" + str(e))
