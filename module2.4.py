numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num in numbers:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        primes.append(num)
    else:
        not_primes.append(num)
        if num == 1:
         not_primes.remove(num)
print("Список простых чисел:")
print(primes)
print("\nСписок непростых чисел:")
print(not_primes)