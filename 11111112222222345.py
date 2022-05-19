a = input("Введите пароль: ")
if len(a) >= 8 and not a.isupper() and not a.islower() and not a.isalpha() and not a.isdigit():
    print("Сложный :)")
elif len(a) >= 8 and a.islower() and not a.isalpha():
    print("Средний ^-^")
elif len(a) >= 8 and (a.isalpha()) or a.isdigit():
    print("Простой :(")
else:
    print("Очень простой *_*")