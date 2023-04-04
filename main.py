from random import choice


class Password:
    chars = ""

    @staticmethod
    def generate_password():
        password = ''
        for j in range(length):
            password += choice(Password.chars)
        return password

    def digits(self):
        digits = '0123456789'
        if self == 'да':
            Password.chars += digits

    def lowercase_letters(self):
        lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        if self == 'да':
            Password.chars += lowercase_letters

    def uppercase_letters(self):
        uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self == 'да':
            Password.chars += uppercase_letters

    def punctuation(self):
        punctuation = '!#$%&*+-=?@^_'
        if self == 'да':
            Password.chars += punctuation

    def ignore(self):
        if self == 'да':
            for i in 'il1Lo0O':
                Password.chars = Password.chars.replace(i, '')


while 1:
    try:
        numbers_of_generations = int(input("Введите кол-во генерируемых паролей: "))
        length = int(input("Введите длину паролей: "))
    except ValueError:
        print("Попробуйте еще раз. В этот раз введите число!")

    print("\nДля согласия пишите 'Да', а в противоположном случае - ничего")
    Password.digits(input("Включать цифры - ' 1234567890 ': ").lower())
    Password.uppercase_letters(input("Включать прописные - ' ABCDEFGHIJKLMNOPQRSTUVWXYZ ': ").lower())
    Password.lowercase_letters(input("Включать строчные - ' abcdefghijklmnopqrstuvwxyz ': ").lower())
    Password.punctuation(input("Включать символы - ' !#$%&*+-=?@^_ ': ").lower())
    Password.ignore(input("Исключать неоднозначные символы - ' il1Lo0O ': ").lower())
    for _ in range(numbers_of_generations):
        print(Password.generate_password())

    print("\nМожете повторить запрос написав 'Да' или же ничего, НО тогда программа закроется:", end=" ")
    if input().lower() == "да":
        print()
        Password.chars = chars = ""
    else:
        print("Пока!")
        break
