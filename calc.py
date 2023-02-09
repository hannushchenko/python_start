def num2calc():
    inputnum = input("Enter 2 num: ")
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


def num16calc():
    checklist16num = ['0','1','2','3',
                      '4','5','6','7',
                      '8','9','a','b',
                      'c','d','e','f']

    inputnum = input("Enter num16: ")
    res = 0
    work = True
    inputnumlen = len(inputnum)

    for symb in inputnum:
        if str(symb) in checklist16num:
            intsymb = checklist16num.index(symb)
            res = res + intsymb * pow(16, inputnumlen-1)
            inputnumlen = inputnumlen - 1
        else:
            print("error")
            work = False
            break
    if work:
        print(res)


def menu():
    repeat = True
    mode_now = True
    while repeat:
        print(f"You are in {'2x' if mode_now else '16x' } calculation mode.")

        choice = input("Type 'c' to change mode, or 'q' to exit: ")
        if choice.lower() == "c":
            mode_now = not mode_now
        elif choice.lower() == 'q':
            repeat = False
        else:
            pass

        if mode_now==True:
            num2calc()
        else:
            num16calc()


menu()