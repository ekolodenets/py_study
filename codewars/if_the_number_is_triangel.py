'''
if the number is triangle:
6 = True
  1
 2 3
4 5 6

8 = False
   1
  2 3
 4 5 6
7 8

"hello!" = False

'''


def is_triangle_number(number):
    if type(number) == int:
        step = 1
        while True:

            if number < 0:
                return False
            if number == 0:
                return True
            number -= step
            step += 1

    else:
        return False


# print(is_triangle_number(367))
# assert is_triangle_number(3) == True
# assert is_triangle_number(5) == False
# assert is_triangle_number("hello!") == False
# assert is_triangle_number(6.15) == False
# assert is_triangle_number(13686) == False
# assert is_triangle_number(63882.132740285575) == False
# assert is_triangle_number(367) == False
# assert is_triangle_number(False) == False
# assert is_triangle_number(True) == False
