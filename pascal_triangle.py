def triangle(y):
    triangle = []
    for i in range(y):
        triangle.append([])
        for j in range(i+1):
            if j == 0 or j == i:
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
        
    for i in triangle:
        print(i)

def try_start():
    try:
        triangle(int(input('Введите количество строк: '))) 
    except Exception as _ex:
        print('Введите число!') 
        try_start()

try_start()
