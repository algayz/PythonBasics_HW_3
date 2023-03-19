import random
N = int(input("Введите размер массива: "))
X = int(input("Введите число X: "))
N_array = []

for i in range(N):
    N_array.append(random.randint(0, N//2))

print(f"{N_array} массив")

count = 0
for i in N_array:
    if i == X:
        count += 1
print(f"{X} встречается {count} раз ")