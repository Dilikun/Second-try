import random

lowDigit = 10
highDigit = 50
digit = 0

countInput = 0
win = False
playGame = True
x = 0
startScore = 100
score = 0
maxScore = 0

while playGame:
    digit = random.randint(lowDigit, highDigit)
    print(f'Number is {digit}')
    print('-' * 30)
    countInput = 0
    score = startScore
    while not win and score > 0:
        print('-' * 30)
        print(f'Заработано очков {score}')
        print(f'Рекорд {maxScore}')

        x = ""
        while not x.isdigit():
            x = input(f'Введите число от {lowDigit} до {highDigit}: ')
            if not x.isdigit():
                print('+' * 30 + 'Ведите число!')


        x = int(x)
        if x == digit:
            win = True
        else:
            length = abs(x - digit)
            if length < 3:
                print('very Close')
            elif length < 5:
                print('Close')
            elif length < 10:
                print('little close')
            elif length < 15:
                print('cold')
            elif length < 20:
                print('too cold')
            else:
                print('cold wind')

            if countInput == 7:
                score -= 10
                if digit % 2 ==0:
                    print('Number is even')
                else:
                    print('Number is odd')
            elif countInput == 6:
                score -= 8
                if digit % 3 == 0:
                    print('Число кратно 3')
                else:
                    print('Число не кратно 3')
            elif countInput == 5:
                score -= 4
                if digit % 4 == 0:
                    print('Число кратно 4')
                else:
                    print('Число не кратно 4')
            elif 2 < countInput < 5:
                score -= 2
                if x > digit:
                    print('Число меньше вашего')
                elif x < digit:
                    print('Число больше вашего')

        score -= 3
        countInput += 1
    print("*" * 40)
    if x == digit:
        print("Congrats You win!!!")
    else:
        print('Your score is 0')

    if input("Enter - try again, 0 - exit: ") == 0:
        playGame = False
    else:
        win = True

    if score > maxScore:
        maxScore = score
