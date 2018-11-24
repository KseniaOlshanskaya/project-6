def cals(y, z, w):
    result = (10 * z + 6.25 * w - 5 * y)
    return result


def total_result(result, e):
    if e == 1:
        total_result = result * 1.6375
    elif e == 2:
        total_result = result * 1.375
    else:
        total_result = result * 1.2
    return total_result


def diet(x):
    result = x * 0.8
    return result


def fast_diet(x):
    result = x * 0.6
    return result


def main():
    print("Узнайте, сколько калорий Вам нужно потреблять в день:\n")
    try:
        gender = input('Введите пол. Если вы женщина введите "ж", мужчина -  "м": ').lower()
        while gender != "ж" and gender != "м":
            gender = input('Вы ввели неверное значение. '
                           'Если вы женщина введите "ж", мужчина -  "м": ').lower()

        age = int(input('Сколько Вам полных лет?: '))

        weight = float(input('Введите свой вес (в киллограммах): '))

        height = float(input('Введите свой рост (в сантиметрах): '))

        print('Как часто вы занимаетесь спортом (физкультурой)?')
        exercise = int(input('Введите: 1 - если часто; 2 - редко; 3 - вообще не занимаюсь: \n'))
        while exercise != 1 and exercise != 2 and exercise != 3:
            exercise = int(input('Вы ввели неверное значение. Введите: 1 - если часто; 2 - редко;'
                             ' 3 - вообще не занимаюсь: '))

        result = cals(age, weight, height)

        if gender == "ж":
            result -= 161
        elif gender == "м":
            result += 5

        result = total_result(result, exercise)
        print("Ваша суточная норма калорий = ", round(result), "ккал")

        result = diet(result)
        print("Чтобы похудеть = ", round(result), "ккал")

        result = fast_diet(result)
        while result <= (weight / 0.45) * 8:
            result += 1
        print("Быстрое похудение = ", round(result), "ккал")

    except ValueError:
        print('Вы ввели неверное значение. Перезапустите программу для повторного рассчета.')


if __name__ == "__main__":
    main()
