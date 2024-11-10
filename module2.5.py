def get_matrix(n, m, value):

    matrix = []

    # Добавляем пустые списки для строк
    for _ in range(n):
        matrix.append([])

    # Заполняем матрицу значениями value
    for i in range(n):
        for _ in range(m):
            if value <= 0:
                return []
            matrix[i].append(value)

    return matrix


# Пример использования функции
result1 = get_matrix(2, 2, 0)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, -3)

print(result1)
print(result2)
print(result3)
