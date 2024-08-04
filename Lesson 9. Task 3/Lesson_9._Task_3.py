a=set()
for i in input("Введите последовательность чисел через пробел - ").split():
    if i not in a:
       a.add(i)
       print('NO')
    else:
        print('YES')


    