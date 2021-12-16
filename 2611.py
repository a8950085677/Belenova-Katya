# Большее из пяти чисел
def bid(x, y):	# Процедура большее из двух
    global z        # глобальная переменная
    if x>y: z=x
    else:   z=y
# Основная программа
print("Введите 5 чисел через пробел")
a,b,c,d,e = input().split()
a,b,c,d,e = int(a), int(b), int(c), int(d), int(e)
bid(a, b)
bid(z, c)
bid(z, d)
bid(z, e)
print("Максимальное число")
   