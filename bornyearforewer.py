print("Напиши день, месяц и год рождения А.С.Пушкина, а я буду подсказывать если ты ошибёшься)")

# Угадать дату рождения

day = int(input("Введите день рождения А.С.Пушкина: "))
birthday = 6

while day != birthday:                              # Повторение цикла
    day = int(input("Неверно попробуй ещё раз: "))

if day == birthday:
    print("Верно")
else:
    print(day)

# Угадай месяц

month = str(input("Напиши месяц рождения А.С.Пушкина: "))
month_of_birth = "июнь"

while month != month_of_birth:                              # Повторение цикла
    month = str(input("Неверно попробуй ещё раз: "))

if month_of_birth == month:
    print("Верно")
else:
    print(month)

# Угадай год

yahr = int(input("Напиши год рождения А.С.Пушкина: "))
yahr_of_birth = 1799

while yahr != yahr_of_birth:                              # Повторение цикла
    yahr = int(input("Неверно попробуй ещё раз: "))

if day == birthday:
    print("Верно")
else:
    print(yahr)

print("Дата рождения А. С. Пушкина: ", birthday,  "июня", yahr_of_birth, "года")