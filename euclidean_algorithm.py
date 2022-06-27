from random import randint
import time

# # Slow algorithm:
# def alg(a, b):
#     val1 = a
#     val2 = b
#     a, b = abs(a), abs(b)
#     while a!=b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     print(f'Greatest common divisor of numbers {val1} и {val2} = {a}')
#     return a

# Fast algorithm:
def alg(a, b):
    val1 = a
    val2 = b
    a, b = abs(a), abs(b)

    if a > b:
        a, b = b, a

    while b != 0:
        a, b = b, a%b

    print(f'Greatest common divisor of numbers {val1} и {val2} = {a}')

#Testing func
def test_alg(func):
    a, b = 28, 35
    res = func(a, b)
    print('Test #1 OK', res) if res == 7 else print('Test #1 NOT OK', res)

    a, b = 1, 100
    res = func(a, b)
    print('Test #2 OK', res) if res == 1 else print('Test #2 NOT OK', res)

    a, b = 100000000, 15
    st = time.time() #startTime
    res = func(a, b)
    et = time.time() #endTime
    dt = et - st #timeDefinition
    print('Test #3 OK', res, 'Time = ', dt) if res == 5 else print('Test #3 NOT OK', res, 'Time = ', dt)

    for i in range(5):
        a, b = randint(-100000, 100000), randint(-100000, 100000)
        st = time.time() #startTime
        res = func(a, b)
        et = time.time() #endTime
        dt = et - st #timeDefinition
        print(f'Random int test #{i+1} {res} time = {dt}')


def start():
    if input('Input "test" for testing: ') == "test":
        test_alg(alg) 
        exit()
    print('Enter two numbers to find the greatest common divisor:')
    
    def start_input():
        try:
            a = int(input('First value - '))
            b = int(input('Second value - '))
            if a == 0 or b == 0:
                print("Number must not be zero")
                start_input()
            alg(a, b)
        except Exception:
            print('You need to enter a number')
            start_input()
    start_input()

start()