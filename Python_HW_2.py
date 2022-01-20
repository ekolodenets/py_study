import math
print("_"*57, '\n', "-"*25, "1-4", "-"*25)
item_1 = 66   #  1. Создать переменную item_1 типа integer.
item_2 = 20   #  2. Создать переменную item_2 типа integer.
result_sum = item_1 + item_2    #  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
print(result_sum)    #  4. Вывести result_sum в консоль.

print("_"*57, '\n', "-"*25, "5-6", "-"*25)
result_subtr = item_1 - item_2    #  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
print(result_subtr)    #  6. Вывести result_subtr в консоль.

print("_"*57, '\n', "-"*25, "7-8", "-"*25)
result_multi = item_1*item_2    #  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
print(result_multi)    #  8. Вывести result_multi в консоль.

print("_"*57, '\n', "-"*25, "9-10", "-"*24)
result_exp = item_1**item_2    #  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
print(result_exp)    #  10. Вывести result_exp в консоль.

print("_"*57, '\n', "-"*24, "11-12", "-"*24)
result_m_exp = math.pow(item_1, item_2)    #  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
print(result_m_exp)    #  12. Вывести result_m_exp в консоль.

print("_"*57, '\n', "-"*24, "13-14", "-"*24)
result_s_root = item_1**0.5    #  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
print(result_s_root)    #  14. Вывести result_s_root в консоль.

print("_"*57, '\n', "-"*24, "15-16", "-"*24)
result_m_s_root = math.sqrt(item_1)   #  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
print(result_m_s_root )    #  16. Вывести result_m_s_root в консоль.

print("_"*57, '\n', "-"*24, "17-18", "-"*24)
result_mp_s_root = math.pow(item_2, 0.5)    #  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
print(result_mp_s_root)    #  18. Вывести result_mp_s_root в консоль.

print("_"*57, '\n', "-"*24, "19-22", "-"*24)
item_1 = 33    #  19. Присвоить переменной item_1 odd значение
item_2 = 12    #  20. Присвоить переменной item_2 even значение
result_division = item_1/item_2    #  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
print(result_division)    #  22. Вывести result_division в консоль.

print("_"*57, '\n', "-"*24, "23-24", "-"*24)
result_m_floor = math.floor(result_division)   #  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
print(result_m_floor)    #  24. Вывести result_m_floor в консоль.

print("_"*57, '\n', "-"*24, "25-26", "-"*24)
result_m_ceil = math.ceil(result_division)    #  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
print(result_m_ceil)    #  26. Вывести result_m_ceil в консоль.

print("_"*57, '\n', "-"*24, "27-28", "-"*24)
result_int = int(round(result_division))    #  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
print(result_int)  #  28. Вывести result_int в консоль.

print("_"*57, '\n', "-"*24, "29-30", "-"*24)
result_no_division_loss = item_1//item_2    #  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
print(result_no_division_loss)    #  30. Вывести result_no_division_loss в консоль.

print("_"*57, '\n', "-"*24, "31-32", "-"*24)
result_division_loss = item_1%item_2    #  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
print(result_division_loss)    #  32. Вывести result_division_loss в консоль.

print("_"*57, '\n', "-"*24, "33-35", "-"*24)
item_3 = 22    #  33. Создать переменную item_3 и присвоить ей целое число
item_3 += 10    #  34. Прибавить 10 к item_3 с присвоением.
print(item_3)    #  35. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "36-37", "-"*24)
item_3 -= 5    #  36. Отнять 5 от item_3 с присвоением.
print(item_3)    #  37. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "38-39", "-"*24)
item_3 *= 3    #  38. Умножить item_3 на 3 с присвоением.
print(item_3)    #  39. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "40-41", "-"*24)
item_3 /= 2    #  40. Разделить item_3 на 2 с присвоением.
print(item_3)    #  41. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "42-43", "-"*24)
item_3 **= 2    #  42. Возвести в степень 2 item_3 с присвоением.
print(item_3)    #  43. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "44-45", "-"*24)
item_3 **= 0.5    #  44. Найти квадратный корень item_3 с присвоением.
print(item_3)    #  45. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "46-47", "-"*24)
item_3 %= item_3    #  46. Присвоить остаток от деления item_3
print(item_3)    #  47. Вывести item_3 в консоль.

print("_"*57, '\n', "-"*24, "48-51", "-"*24)
b_item_t = True #  48. Создать переменную b_item_t и присвоить True
b_item_f = False    #  49. Создать переменную b_item_f и присвоить False
b_item_result_sum = b_item_f + b_item_f    #  50. Создать переменную b_item_result_sum и присвоить сумму b_item_t и b_item_f
print(b_item_result_sum)    #  51. Вывести b_item_result_sum в консоль.

print("_"*57, '\n', "-"*24, "52-53", "-"*24)
b_item_relult_subtr = b_item_t - b_item_f    #  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
print(b_item_relult_subtr)    #  53. Вывести b_item_relult_subtr в консоль.

print("_"*57, '\n', "-"*24, "54-55", "-"*24)
b_item_relult_multi = b_item_t * b_item_f    #  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
print(b_item_relult_multi)    #  55. Вывести b_item_relult_multi в консоль.

print("_"*57, '\n', "-"*24, "56-57", "-"*24)
try:
    b_item_result_division = b_item_t / b_item_f    #  56. Создать переменную b_item_result_division и присвоить деление b_item_t и b_item_f
except ZeroDivisionError as e:
    print(e)    #  57. Вывести b_item_result_division в консоль. (Получить ошибку)

print("_"*57, '\n', "-"*24, "58-59", "-"*24)
b_item_1_int = int(b_item_t)    #  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
print(b_item_1_int)    #  59. Вывести b_item_1_int в консоль.

print("_"*57, '\n', "-"*24, "60-61", "-"*24)
b_item_2_int = int(b_item_f)    #  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
print(b_item_2_int)    #  61. Вывести b_item_2_int в консоль.