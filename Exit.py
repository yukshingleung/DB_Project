# 5.Exit (exit function)


def exit():
    # while(1):
    #     try:
    #         n = int(input(' Press 0 to return menu: '))
    #         if n != 0:
    #             print('Invalid Option')
    #         else:
    #             break
    #     except:
    #         print('Invalid Option')

    # run()
    n = int(input(' Press 0 to return menu: '))
    if n == 0:
        from mysql_test import run
        run()
    else:
        print('Invalid Option')
        exit()
