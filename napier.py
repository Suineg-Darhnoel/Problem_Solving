def napier(n_decimal):
    numerators = [1] * n_decimal
    denumerators = [n_decimal-i+1 for i in range(n_decimal)]
    print("2.")

    for i in range(n_decimal):
        lift_up = 0
        numerators = [10*i for i in numerators]
        for index, (n, d) in enumerate(zip(numerators, denumerators)):
            numerators[index] = (n+lift_up) % d
            lift_up = (n+lift_up) // d
        print(lift_up, end='')


napier(2000)
