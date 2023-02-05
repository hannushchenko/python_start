# list = []
#
# inp_el = 1
#
# if inp_el != 0:
#  inp_el = input(f"Введіть {len(list)} елемент:")
#  list.append(int(inp_el))
#  print(list)
# else:
#  for n in list:
#   print(f"{n}>0") if n > 0 else print(f"{n}<0")

# # Завдання 1
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for n in a:
#  if n<5:
#   print (n)

# Завдання 2! Повернутись(дублікати)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# for n in a:
#  check = n
#  for nn in b:
#   res = nn == check
#   if res:
#    print(nn)

# Завдання 3
# list = [12,25,9,41,-5,0,31,10,-3]
# list.sort(reverse=True)
# print(list)

# Завдання 4
# list_a = [9,3,-3]
# list_b = [34,6,0]
# list_a.extend(list_b)
# list_a.sort()
# print(list_a)

# Завдання 5
# my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
# res = list(my_dict.values())
# res.sort(reverse=True)
# print(res[:3])

# Завдання 6
# input_word = input("word: ")
#
# temp_list = list(input_word)
# reversed_word =""
#
# for n in range(len(temp_list)):
#  reversed_word += temp_list.pop()
#
# print(f"reverse: {reversed_word}")
#
# if input_word ==reversed_word:
#  print("PALINDROM!")
# else:
#  print("NOT")

# Завдання 7

# seconds = int(input("enter seconds: "))
#
# def calc(seconds):
#
#     minutes = 0
#     hours = 0
#     days = 0
#
#     while seconds > 59:
#         minutes += 1
#         seconds -= 60
#
#     while minutes > 59:
#         hours += 1
#         minutes -= 60
#
#     while hours > 23:
#         days += 1
#         hours -= 24
#
#     if days != 0:
#         print(f"{str(days)}", end=' ')
#         if days % 10 == 1 and days % 100 != 11:
#             print('день', end=' ')
#         elif days % 10 in [2,3,4] and days % 100 not in[12,13,14]:
#             print('дні', end=' ')
#         else:
#             print('днів', end=' ')
#
#     print(f"{str(hours).rjust(2,'0')}:"
#           f"{str(minutes).rjust(2, '0')}:"
#           f"{str(seconds).rjust(2,'0')}")
#     return minutes, hours, seconds, days
#
# calc(seconds)

# Завдання 8
#
# nums = input("enter numbers: ")
#
# replace_nums = nums.replace(' ', '')
#
# print(replace_nums)
# nums_list = replace_nums.split(",")
# print(nums_list)
# set_num = set(nums_list)
# print(set_num)

# Завдання 9
# N = int(input("N рядів трикутника Паскаля:"))
# T = []
# for i in range(N):
#     row = T.append([])
#     for j in range(i+1):
#         el = T[i].append(1)
#         if i!=1 and i!=N and j!=i and j!=0:
#             T[i][j] = T[i-1][j-1] + T[i-1][j]
# print(T)

