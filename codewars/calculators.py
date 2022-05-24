
# Type 1
# while True:
#     a = input().split()
#     try:
#         a[0] = float(a[0]) if '.' in a[0] else int(a[0])
#         a[2] = float(a[2]) if '.' in a[2] else int(a[2])
#     except:
#         print('Please input two numbers')
#     finally:
#         x = a[0]
#         y = a[2]
#         j = {'+': x + y, '-': x - y, '*': x * y, '/': x / y, '**': x ** y, '%': x % y, '//': x // y}
#         if a[1] in j:
#             print(j[a[1]])
#         else:
#             print('Wrong operator')



# Type 2
# import json
# while True:
#     a = input().split()
#     x = json.loads(a[0])
#     y = json.loads(a[2])
#     j = {'+': x + y, '-': x - y, '*': x * y, '/': x / y, '**': x ** y, '%': x % y, '//': x // y}
#     if a[1] in j:
#         print(j[a[1]])
#     else:
#         print('Wrong operator')



# Type 3
# while True:
#     print(eval(input()))



