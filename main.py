import random
def secure(choice):
    if choice.isdigit():
        if 1 <= int(choice) <= 100:
            return True
    return False


def ans(answ):
    if answ.lower() in ['д', 'y']:
        return True
    elif answ.lower() in ['н', 'n']:
        return False
    else:
        print("Ошибка ввода! попробуйте снова >", end='')
        a = input()
        ans(a)
def begin():
    print('Привет, приветствую тебя в игре "Узнавайка"', 'Попробуй угадать загаданное число от 1 до 100', sep=' ')
    number = random.randint(1, 100)
    while True:
        print('Введите число >', end='')
        choice = input()
        if secure(choice) == False:
            print('Ошибка ввода', end='')
            continue
        guess = int(choice)
        if guess > number:
            print('Введенное число больше загаданного')
            continue
        elif guess < number:
            print('Введенное число меньше загаданного')
            continue
        if guess == number:
            print('Поздравляю, вы угадали!', 'Хотите сыграть еще? (y/n)', sep='\n')
            answer = input()
            if ans(answer):
                continue
            else:
                print('Спасибо за игру!')
                break


begin()