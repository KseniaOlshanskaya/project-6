def women_cals(y, z, w):
    result = (10 * z + 6.25 * w - 5 * y - 161)
    return str(result)

def men_cals(y, z, w):
    result = (10 * z + 6.25 * w - 5 * y + 5)
    return str(result)


def main():
    print("Узнайте, сколько калорий Вам нужно потреблять в день:\n")
    try:
        gender = input('Введите пол. Если вы женщина введите "ж", мужчина -  "м": ').lower()
        while gender != "ж" and gender != "м":
            gender = input('Вы ввели неверное значение. Если вы женщина введите "ж", мужчина -  "м": ').lower()
        age = int(input('Сколько Вам полных лет?: '))
        weight = float(input('Введите свой вес (в киллограммах): '))
        height = float(input('Введите свой рост (в сантиметрах): '))
        print('Как часто вы занимаетесь спортом (физкультурой)?')
        exercise = input('Введите: 1 - если часто; 2 - редко; 3 - вообще не занимаюсь: ')
        if gender == "ж" and exercise:
            result = women_cals(age, weight, height)
        elif gender == "м":
            result = men_cals(age, weight, height)

    except ValueError:
        print('Вы ввели неверное значение. Перезапустите программу для повторного рассчета.')
if __name__ == "__main__":
    main()
