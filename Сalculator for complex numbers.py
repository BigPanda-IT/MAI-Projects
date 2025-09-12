print("Введите аргументы для двух комплексных чисел: ");
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print("a = ", a, "b = ", b)
print("c = ", c, "d = ", d)

print("Выберите необходимое действие над комплексными числами: ")
print("1) Сложение")
print("2) Вычитание")
print("3) Умножение")
print("4) Деление")

k = int(input())

ac = a + c
bd = b + d

if k == 1:
    print("Выполнение сложения:")
    ac = a + c
    bd = b + d
    if (bd > 0 and ac != 0):
        print("(a + b*i) + (c + d*i) = ", a + c, "+", b + d, "* i")
    elif (bd < 0 and ac != 0):
        print("(a + b*i) + (c + d*i) = ", a + c, b + d, "* i")
    elif (ac == 0 and bd == 0):
        print("(a + b*i) + (c + d*i) = ", 0)
    elif (bd == 0):
        print("(a + b*i) + (c + d*i) = ", a + c)
    elif (ac == 0):
        print("(a + b*i) + (c + d*i) = ", b + d, "* i")

elif k == 2:
    print("Выполнение вычитания:")
    ac = a - c;
    bd = b - d;
    if (ac != 0 and bd > 0):
        print("(a + b*i) - (c + d*i) = ", (a - c), "+", (b - d), "* i")
    elif (ac != 0 and bd < 0):
        print("(a + b*i) - (c + d*i) = ", (a - c), (b - d), "* i")
    elif (ac == 0 and bd == 0):
        print("(a + b*i) - (c + d*i) = ", 0)
    elif (ac == 0):
        print("(a + b*i) - (c + d*i) = ", b - d, "i")
    elif (bd == 0):
        print("(a + b*i) - (c + d*i) = ", a - c)

elif k == 3:
    print("Выполнение умножения:")
    if ((a * c - b * d) != 0 and (b * c + a * d) > 0):
        print("(a + b*i) * (c + d*i) = ", (a * c - b * d), "+", b * c + a * d, "* i")
    elif ((a * c - b * d) != 0 and (b * c + a * d) < 0):
        print("(a + b*i) * (c + d*i) = ", (a * c - b * d), b * c + a * d, "* i")
    elif ((a * c - b * d) == 0 and (b * c + a * d) == 0):
        print("(a + b*i) * (c + d*i) = ", 0)
    elif ((a * c - b * d) == 0):
        print("(a + b*i) * (c + d*i) = ", b * c + a * d, "* i")
    elif ((b * c + a * d) == 0):
        print("(a + b*i) * (c + d*i) = ", a * c - b * d)

elif k == 4:
    print("Выполнение деления:")
    if (c != 0 and d != 0):
        if ((a * c + b * d) != 0 and (a * d - b * c) > 0):
            print("(a + b*i) / (c + d*i) = ", (a * c + b * d) / (c * c + d * d), "-", (a * d - b * c) / (c * c + d * d), "* i")
        elif ((a * c + b * d) != 0 and (a * d - b * c) < 0):
            print("(a + b*i) / (c + d*i) = ", (a * c + b * d) / (c * c + d * d), "+", abs((a * d - b * c) / (c * c + d * d)), "* i")
        elif ((a * c + b * d) == 0 and (a * d - b * c) == 0):
            print("(a + b*i) / (c + d*i) = ", 0)
        elif ((a * c + b * d) == 0):
            print("(a + b*i) / (c + d*i) = ", -((a * d - b * c) / (c * c + d * d)), "* i")
        elif ((a * d - b * c) == 0):
            print("(a + b*i) / (c + d*i) = ", (a * c + b * d) / (c * c + d * d), "* i")
    else:
        print("Ошибка. Введите корректные данные в новом запросе.")
else:
    print("Ошибка. Выполните запрос заново.")





