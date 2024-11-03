import random
from matplotlib import pyplot as plt
from zad_2.fun.testFunctionParameters import testFunctionParameters as tfp
from zad_2.algo.sa import sa

#functions = [tfp.EXAMPLE1, tfp.EXAMPLE2, tfp.EXAMPLE4, tfp.EXAMPLE5]
functions = [tfp.EXAMPLE1]
repetitions = 10
step_size = 100

for fun in functions:
    print("Function {}".format(fun))
    history = []
    name, objective_func, dim, lb, ub, T, alpha, k, max_iter = fun.value
    for i in range(repetitions):
        init_solution = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        current = sa(init_solution, objective_func, T, alpha, k, max_iter, step_size)
        history.append(current)
        print("History {}".format(current))
        print("History len {}".format(len(current)))
    dlugosci = [len(run) for run in history]
    srednia_dlugosc = sum(dlugosci) / len(dlugosci)
    print("SREDNIA LEN {}".format(srednia_dlugosc))


