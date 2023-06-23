print("Напиши день, месяц и год рождения А.С.Пушкина, а я буду подсказывать если ты ошибёшься)")

# Введение дня рождения
day = int(input("Введите день рождения А.С.Пушкина: "))
birthday = 6

if day == birthday:
    print("Верно")
else:
    print("Не верно указан день")
# Введение месяца рождения
month = str(input("Напиши месяц рождения А.С.Пушкина: "))
month_of_birth = "июнь"
if month_of_birth == month:
    print("Верно")
else:
    print("Не верно указан месяц")


 # Введение года рождения
yahr = int(input("Напиши год рождения А.С.Пушкина: "))
yahr_of_birth = 1799
if yahr_of_birth == yahr:
   print("Верно")
else:
   print("Не верно указан год")

