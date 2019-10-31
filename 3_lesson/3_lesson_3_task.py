def my_func(par_1, par_2, par_3):
    n = (par_1, par_2, par_3)
    i = min(n)  # так и не понял как обойтись без этого переобразования n->i
    return par_1 + par_2 + par_3 - i

print(my_func(70, 25, 210))