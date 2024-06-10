numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
for i in numbers:
    is_prime = True
    if i <= 1:
        print('число является ни простым ни составным')
        continue
    for j in range(2, i):
        if i % j == 0:  # если число имеет делитель с остатком 0
            is_prime = False  # то число не является простым
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('not_primes: ', not_primes)
