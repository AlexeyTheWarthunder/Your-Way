import random
import time


def job100000(money):
    for i in range(9):
        tusk_1 = random.randint(100, 999)
        tusk_2 = random.randint(100, 999)
        print("Решите задачу.")
        print(tusk_1, "*", tusk_2, "= ?")
        answer = input()
        while answer != str(tusk_1 * tusk_2):
            print("Введите число - ответ на задачу.")
            answer = input()
        money += 100000
        print("Вы заработали 100 тыс. рублей!")
        print("\n")


def it_job(money):
    while money < 10000000:
        a = random.randint(-1000, 1000)
        while a == 0:
            a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        c = random.randint(-1000, 1000)
        asi = ""
        bs = ""
        cs = ""
        if b > -1:
            bs = "+"
        if c > -1:
            cs = "+"
        print(asi + str(a) + "x\u00b2" + bs + str(b) + "x" + cs + str(c))
        discriminant = b ** 2 - 4 * a * c
        if discriminant >= 0:
            x1 = (-b - discriminant ** 0.5) / (2 * a)
            x2 = (-b + discriminant ** 0.5) / (2 * a)
            x1 = round(x1, 3)
            x2 = round(x2, 3)
            x1 = str(x1)
            x2 = str(x2)
        else:
            x1 = "нет корней"
            x2 = "нет корней"
        xset = {x1, x2}
        print("Введите два числа - корни уравнения, " +
              "округлив их до тысячных (если они есть) и" +
              " \"нет корней\" строчными буквами, если их нет.")
        x1i = input()
        x2i = input()
        while x1i not in xset and x2i not in xset:
            print("Введите два числа - корни уравнения (если они есть) и" +
                  " \"нет корней\" строчными буквами, если их нет.")
            x1i = input()
            x2i = input()
        print("Вы заработали 350 тыс. рублей!")
        print("\n")
        money += 350000


def job_shop(money):
    money_count = 0
    for i in range(63):
        cost = random.randint(1, 1000000)
        money_count += cost
        print("Покупка: +", cost, sep="")
        print("Выведите число - количество денег в кассе.")
        shop_money = input()
        while shop_money != str(money_count):
            print("Выведите число - количество денег в кассе.")
            shop_money = input()
        money += 42000
        print("Вы заработали 42 тыс. рублей!")
        print("\n")
    return money

army = False
burn = False
money = 3000
inventory = [money]
print("Как вас зовут?")
name = input()
dream_var = ["автомобиль", "частный вертолет", "вилла в Испании", "компьютер"]
dream = random.choice(dream_var)
print("\n")
print("Ваша мечта - ", dream,\
      ", за неё придется заплатить 10 млн рублей.\n", sep="")

print("Из воспоминаний ", name, ":", sep="")
print("\n08.08.2007, Утро")
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
    burn_choise = input()
    while burn_choise != "1" and burn_choise != "2":
        print("Введите 1 или 2.")
        burn_choise = input()
    if burn_choise == "1":
        print("Необходимо сначала подключить тариф. Подключить?")
        print("1. Да")
        print("2. Нет")
        no_choise = input()
        print("Поздно. У вас уже нет выбора. Подключение...")
        time.sleep(3)
        print("Подключено.")
        print("К сожалению, вы не успели ответить," +
              "и принимаете решение перезвонить.")
        print("Звонок...")
        time.sleep(5)
        print("Соединение")
        time.sleep(5)
        print("Тимур Фархадович: Почему не на работе? Сколько можно уже? Ты уволен.")
        print("Вы уволены с работы. Вам предоставлена" +
              "выплата в размере 50 тыс. рублей")
    else:
        print("Вы уволены с работы.")
    burn = True

print("Из воспоминаний ", name, ":", sep="")
print("\n")
print("08.08.2007, Вечер")
print("Я помню, как сидел на кухне и смотрел телевизор, когда" +
      "мой покой прервал телефонный звонок. Это был мой лучший" +
      "друг Иван. Он пригласил меня в гости, ведь у него сегодня" +
      "День рождения, а отметить не с кем.")

print("1. Согласиться и пойти за подарком")
print("2. Не согласиться и не идти за подарком")
gift_choise = input()
while gift_choise != "1" and gift_choise != "2":
    print("Введите 1 или 2.")
    gift_choise = input()

if gift_choise == "1":
    print("Выбор за вами:")
    print("1. Заказать на Homeberries")
    print("2. Сходить в магазин")
    buy_choise = input()
    while buy_choise != "1" and buy_choise != "2":
        print("Введите 1 или 2.")
        buy_choise = input()
    if buy_choise == "1":
        print("С вас 1800 рублей.")
        if money >= 1800:
            money -= 1800
            print("Homeberries: оплата. -1800 рублей.")
        else:
            print("Недостаточно средств")
            exit()
        if not burn:
            print("Раздался звонок в дверь. Вы видите курьера, стоящего у двери." +
                  " Он вручает вам ваш заказ и рассказывает жестокую правду.")
            print("* КУРЬЕР БЫЛ ВОЕНКОМОМ *")
            army = True
    else:
        print("Зайдя в магазин, вы сразу приметили нужную вещь.")
        print("Кассир: С вас 1500 рублей.")
        money -= 1500
        if not burn:
            print("Как только вы выходите из магазина," +
                " вас останавливают двое людей в военной форме," +
                " и вы сразу понимаете, насколько вы невезучий.")
            army = True

    if not burn:
        print("Из воспоминаний ", name, ":", sep="")
        print("\n")
        print("09.08.2007, Раннее утро")
        print("Я стоял и ждал решения комиссии. Разумеется, мне не хотелось " +
            "идти в армию, и в моей голове начали" +
            " появляться нехорошие мысли...")
        print("1. Подкупить комиссию")
        print("2. Смириться со своей судьбой")
        corr_choise = input()
        while corr_choise != "1" and corr_choise != "2":
            print("Введите 1 или 2.")
            corr_choise = input()
        if corr_choise == "1":
            print("\"Ай-ай-ай, как же так?\" - говорит военком." +
                  " \"Молодой человек, вы знаете," +
                  " что коррупция - это плохо?\"")
            print("Вас настигает мгновенная карма, вы отправляетесь в армию.")
        else:
            print("Вы отправляетесь в армию.")
        army = True
else:
    print("Вас настигает мгновенная карма и вы попадаете в армию")

if burn:
    print("Вас уволили с работы и вы понимаете, что нужно найти новую.")
    print("1. Найти новую работу")
    print("2. Остаться безработным")
    job_choice = input()
    while job_choice != "1" and job_choice != "2":
        print("Введите 1 или 2.")
        job_choice = input()
    if job_choice == "1":
        print("Из воспоминаний ", name, ":", sep="")
        print("\n09.08.2007, День")
        print("Я всегда думал, что работа в IT - это интересно," +
              " высокооплачиваемо, безобидно и просто классно." +
              " И вот, у меня появился шанс туда попасть.")
        print("1. Пойти работать в IT по плотному графику")
        print("2. Пойти работать продавцом")
        it_choice = input()
        while it_choice != "1" and it_choice != "2":
            print("Введите 1 или 2.")
            it_choice = input()
        if it_choice == "1":
            it_job(money)
        else:
            money = job_shop(money)
            print("Из воспоминаний ", name, ":", sep="")
            print("\n16.08.2007, Утро")
            print("Я, как обычно, шёл на работу, но на крыльце магазина " +
                  "меня ждал неприятный сюрприз - там стоял военком.")
            army = True
            print("Я тогда подумал: единственным моим " +
                  "шансом остаётся выезд из страны.")
            print("1. Уехать из страны")
            print("2. Остаться")
            country_choice = input()
            while country_choice != "1" and country_choice != "2":
                print("Введите 1 или 2.")
                country_choice = input()
    #         if country_choice == "1":

    # if job_choice == "2":
