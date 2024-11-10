n = int(input("Введите число от 3 до 20: "))
result = []

for i in range(1, n):
    for j in range(1, n):
        if n % (i + j) == 0 and i != j and i < j:
            result.append((i, j))
print(result)
