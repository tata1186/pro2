again = "да"
while again == "да":

    counter_yes = 0  # Задаём счётчик правильных ответов
    counter_no = 0  # Задаём счётчик неправильных ответов

    person1 = input("Введите год рождения А. С. Пушкина: ")

    if person1 == "1799":
        print("Верно")
        counter_yes = counter_yes + 1
    else:
        print("Неверно")
        counter_no = counter_no + 1

    person2 = input("Введите год рождения Л. Н. Толстого: ")

    if person2 == "1828":
        print("Верно")
        counter_yes = counter_yes + 1
    else:
        print("Неверно")
        counter_no = counter_no + 1

    person3 = input("Введите год рождения С. А. Есенин: ")

    if person3 == "1895":
        print("Верно")
        counter_yes = counter_yes + 1
    else:
        print("Неверно")
        counter_no = counter_no + 1

    person4 = input("Введите год рождения М. Ю. Лермонтова: ")

    if person3 == "1814":
        print("Верно")
        counter_yes = counter_yes + 1
    else:
        print("Неверно")
        counter_no = counter_no + 1

    person5 = input("Введите год рождения Ф. М. Достоевского: ")

    if person3 == "1821":
        print("Верно")
        counter_yes = counter_yes + 1
    else:
        print("Неверно")
        counter_no = counter_no + 1

    questions = 5

    print("Верных ответов: ", counter_yes, ",", "что составляет", counter_yes * 100 / questions, "%")
    print("Не верных ответов: ", counter_no, ",", "что составляет", counter_no * 100 / questions, "%")

    again = input("Хочешь сыграть ещё раз? да/нет: ")
print("Благодарим за участие")
