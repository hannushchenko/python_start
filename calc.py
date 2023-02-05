def num2calc():
    inputnum = input("enter 2 num: ")
    list2calc = list(inputnum)
    len2calc = len(list2calc)
    res = 0
    work = True

    for n in list2calc:
        num = int(n)
        if num == 1 or num == 0:
            res = res + num * pow(2, len2calc-1)
            len2calc = len2calc - 1
        else:
            print("error")
            work = False
            break

    if work:
        print(res)

num2calc()

