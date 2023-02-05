# def num2calc():
#     inputNum = input("enter 2 num: ")
#     list2calc = list(inputNum)
#     len2calc = len(list2calc)
#     res = 0
#     work = True
#
#     for n in list2calc:
#         num = int(n)
#         if num == 1 or num == 0:
#             res = res + num * pow(2, len2calc-1)
#             len2calc = len2calc - 1
#         else:
#             print("error")
#             work = False
#             break
#
#     if work:
#         print(res)
#
# num2calc()

def num16calc():
    checkList16num = ['0','1','2','3',
                      '4','5','6','7',
                      '8','9','a','b',
                      'c','d','e','f']

    inputNum = input("enter num16: ")
    res = 0
    work = True
    inputNumLen = len(inputNum)

    for symb in inputNum:
        if str(symb) in checkList16num:
            intSymb = checkList16num.index(symb)
            res = res + intSymb * pow(16, inputNumLen-1)
            inputNumLen = inputNumLen - 1
        else:
            print("error")
            work = False
            break
    if work:
        print(res)

num16calc()

