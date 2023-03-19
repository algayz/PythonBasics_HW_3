n = int(input("Ввелите размер массива "))
list_1 = list()
for i in range(n):
    x = int(input("Введите элементы массива "))
    list_1.append(x)

k = int(input("Введите число, которе будете сравнивать с элементами массива "))
m = abs(k - list_1[0]) 

number = list_1[0]
for i in range(1, len(list_1)):
    if m >= abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(f" Ближайшее число к элементу {k} - {number}")