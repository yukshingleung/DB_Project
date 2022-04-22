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
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='huang741108',
        port=3306,
        db='shopDB',
        charset='utf8'
    )

    if os.name == 'posix':
        sys_com = "clear"
    else:
        sys_com = "cls"
    os.system(sys_com)
    displayMainMenu()
    while True:
        try:
            n = int(input("Enter suitable option: "))
            if n > 10:
                print("Invalid Option")
            else:
                break
        except:
            print("Invalid Option")
    # 1. Add a New Customer
    if n == 1:
        os.system(sys_com)
        addCustomer(conn)
    # 2. Show All Customers
    elif n == 2:
        os.system(sys_com)
        getAllCustomer(conn)
    # 3. Add a New Shop
    elif n == 3:
        os.system(sys_com)
        addShop(conn)
    # 4. Show All Shops
    elif n == 4:
        os.system(sys_com)
        getAllShops(conn)
    # 5. Search Item
    elif n == 5:
        os.system(sys_com)
        searchItem(conn)
    # 6. Show All Items
    elif n == 6:
        os.system(sys_com)
        ShowAllItemWithShop(conn)
    # 7. Add a New Item to a Shop
    elif n == 7:
        os.system(sys_com)
        AddNewItemToShop(conn)
    # 8. Purchase
    elif n == 8:
        os.system(sys_com)
        purchase(conn)
    # 9. Cancel Order
    elif n == 9:
        os.system(sys_com)
        cancel(conn)
    # 10. Exit
    elif n == 10:
        os.system(sys_com)
        print(" - - - Thank You - - - ")
    # else:
    #     os.system(sys_com)
    #     run()

try:
    if __name__ == "__main__":
        run()

except pymysql.Error as e:
    print("Fail to connect to Database" + str(e))
