def pop():
    production = int(input("Введите количесство выроботки: "))
    rate = int(input("Введите сумму ставки часа: "))
    prize = int(input("Введите сумму премии: "))
    return (production * rate) + prize
