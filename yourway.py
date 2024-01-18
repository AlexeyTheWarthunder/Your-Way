import random

def job100000(money):
    tusks = [161, 314, 298, 512, 666, 110, 810, 911,\
             637, 483, 404, 205, 101, 789, 600, 181, 914, 515]
    for i in range(9):
        tusk_1 = random.choice(tusks)
        tusk_2 = random.choice(tusks)
        print("Решите задачу.")
        print(tusk_1, "*", tusk_2, "= ?")
        answer = input()
        while answer != str(tusk_1 * tusk_2):
            print("Введите число - ответ на задачу.")
            answer = input()
        money += 100000


money = 3000
inventory = [money]
print("Как вас зовут?")
name = input()
dream_var = ["автомобиль", "частный вертолет", "вилла в Испании", "компьютер"]
dream = random.choice(dream_var)
print("Ваша мечта - ", dream,\
      ", за него придется заплатить 10 млн рублей.", sep="")

print("Из воспоминаний ", name, ":", sep="")
print("\n08.08.2007")
print("Это был обычный летний день. Я, как обычно, встал в 7 часов утра," +
      "позавтракал и вышел на улицу. Предо мной встал выбор: " +
      "как и все пойти на работу или, махнув на все рукой," +
      "вернуться домой.")
print("1. Пойти на работу")
print("2. Вернуться домой")

first_choise = input()
while first_choise != "1" and first_choise != "2":
    print("Введите 1 или 2.")
    first_choise = input()

if first_choise == "1":
    job100000(money)
elif first_choise == "2":
    print("Вы приходите домой. Внезапно раздаётся телефонный звонок." +
          "Вам звонит Тимур Фархадович - ваш начальник.")
    print("1. Ответить")
    print("2. Сбросить")
    burn_chooise = input()
    while burn_chooise != "1" and burn_chooise != "2":
        print("Введите 1 или 2.")
        burn_chooise = input()
