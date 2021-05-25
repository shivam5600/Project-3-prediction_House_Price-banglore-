
def new_func(n):
    if ((n % 4 ==0) and (n % 100 !=0)) or (n % 400 ==0):
        leap = True
    else:
        leap = False
    print("year is leap:",leap)

new_func(1600)