# Игра "Угадай число"
# Функции:
# 1. На выбор три сложности. Угадывать число в интервале до 10, 20 или 30
# 2. Два типа подсказок: "Больше или меньше" и "Горячо / холодно"
# 3. Определение победил ли игрок в раунде
# 4. Запрос на перезапуск игры после завершения раунда
# 5. Вывод счета побед поражений после завершения игры

from random import randint as r
import cowsay

count_win = 0
count_lose = 0

#Угадай число:
def guess(value, game_type):
    #Определение победы:
    def winner(win_or_not):
        if win_or_not == True:
            global count_win
            print(f'Вы угадали! Это было число {computer_value}')
            cowsay.cow('А вот и наш победитель!')
            count_win += 1
            new_game()
        else:
            global count_lose
            print('Вы не угалали:(')
            count_lose += 1
            new_game()

    print('Ваша сложность: ', value, '. Интервал угадывания: от 1 до ', value*10, '\nУ вас 5 попыток.', sep='')
    computer_value = r(1, value*10)
    print("загаданное число",computer_value) #Отладка
    user_value = 0
    
    #Ввод числа с подсказкой больше или меньше (Тип игры 1):
    def more_or_less():   
        win = False
        for i in range(5):
            try:
                user_value = int(input(f'Попытка #{i+1} Угадай число: '))
                if user_value < computer_value:
                    print('Ваше число меньше загаданного!')
                elif user_value > computer_value:
                    print('Ваше число больше загаданного!')
                elif user_value == computer_value:
                    win = True
                    break
            except ValueError:
                print('Вы ввели не число!')
        winner(win)

    # Ввод числа с подсказкой горячо или холодно (Тип игры 2):
    def cold_or_hot():
        win = False
        for i in range(5):
            try:
                user_value = int(input(f'Попытка #{i+1} Угадай число: '))
                if abs(user_value - computer_value) > 3:
                    print('Холодно')
                elif abs(user_value - computer_value) > 2:
                    print('Тепло')
                elif abs(user_value - computer_value) > 1:
                    print('Очень тепло!')
                elif abs(user_value - computer_value) == 1:
                    print('Горячо!')
                else:
                    win = True
                    break
            except ValueError:
                print('Вы ввели не число!')
        winner(win)
    
    #Запуск игры в зависимости от типа:
    more_or_less() if game_type == 1 else cold_or_hot()

#Функция выбора сложности и выбора типа игры при старте игры:
def start_game():
    # Выбор сложности:
    max = 0
    while max < 1 or max > 3:
        try:
            max = int(input('Выберите сложность: \n1 - до 10 \n2 - до 20 \n3 - до 30 \nСложность: '))
            if max < 1 or max > 3:
                print('Введите число от 1 до 3!')
        except ValueError:
            print('Введите число!')
    
    # Выбор типа игры:
    game_type = 0
    while game_type != 1 or 2:
        try:
            game_type = int(input('Типы игры: \n1 - "Больше или меньше" \n2 - "Горячо или холодно" \nВыберите тип: '))
            if game_type == 1:
                guess(max, 1)
            elif game_type == 2:
                guess(max, 2)
            else:
                print('Введите число от 1 до 2!')
        except ValueError:
            print('Введите число от 1 до 2!')

#Запрос новой раунда и подведение счета в случае завершения:
def new_game():
    new_game = input('Начать игру заново? (Введите "да")')
    start_game() if new_game.lower() == 'да' else print('Победы:', count_win, '\nПоражения:', count_lose), quit()


start_game()