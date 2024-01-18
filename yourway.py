import random

print("Как вас зовут?")
name = input()
dream_var = ["автомобиль", "частный вертолет", "вилла в Испании", "компьютер"]
dream = random.choice(dream_var)
print("Ваша мечта - ", dream,\
        ", за него придется заплатить 10 млн рублей.", sep="")