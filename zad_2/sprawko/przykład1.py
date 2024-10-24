import random
from matplotlib import pyplot as plt
from zad_2.fun.testFunctionParameters import testFunctionParameters as tfp
from zad_2.algo.sa import sa


fun = tfp.EXAMPLE4
print("Function {}".format(fun))
name, objective_func, dim, lb, ub, T, alpha, k, max_iter = fun.value
init_solution = [0]
#init_solution = [random.uniform(lb[i], ub[i]) for i in range(dim)]
best_solution, ile_up = sa(init_solution, objective_func, T, alpha, k, max_iter)
print("Best solution {}".format(best_solution))
print("Best cost {}".format(ile_up))


