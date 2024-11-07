import random
from matplotlib import pyplot as plt
from zad_2.fun.testFunctionParameters import testFunctionParameters as tfp
from zad_2.algo.sa import sa

#functions = [tfp.EXAMPLE1, tfp.EXAMPLE2, tfp.EXAMPLE4, tfp.EXAMPLE5]
functions = [tfp.EXAMPLE5]
repetitions = 10
step_size = 0.5

for fun in functions:
    print("Function {}".format(fun))
    history = []
    name, objective_func, dim, lb, ub, T, alpha, k, max_iter = fun.value
    for i in range(repetitions):
        init_solution = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        current = sa(init_solution, objective_func, T, alpha, k, max_iter, step_size, lb, ub, dim)
        history.append(current)
        #print("History {}".format(current))
        #print("History len {}".format(len(current)))
    dlugosci = [len(run) for run in history]
    srednia_dlugosc = sum(dlugosci) / len(dlugosci)
    for run in history:
        print("history {}".format(run))
        for isbetter in run:
            print("isbetter {}".format(isbetter))

    print(srednia_dlugosc)
    print(objective_func([11.625545, 5.7250444]))

