# 10.Exit (exit function)
def exit():
    while(1):
        try:
            # make sure n is not ""
            n = int(input(' Press 0 to return menu: '))
            break
        except:
            print("Invalid Option")
    if n == 0:
        from mysql_test import run
        run()
    else:
        print('Invalid Option')
        exit()
