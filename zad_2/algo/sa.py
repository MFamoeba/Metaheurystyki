import numpy as np
import random
from zad_2.fun.tools import find_new_best_positions

def explore(current_solution, step_size=0.1):
    return current_solution + np.random.uniform(-step_size, step_size, len(current_solution))

def sa(init_solution, objective_func, initial_temp, alpha, k, max_iter):
    current_solution = np.array(init_solution)
    current_cost = objective_func(current_solution)
    temperature = initial_temp
    best_solution = current_solution
    best_cost = current_cost
    ile_up = 0
    for i in range(max_iter):
        # krok 3
        new_solution = explore(current_solution)
        new_cost = objective_func(new_solution)
        delta_cost = new_cost - current_cost
        boltzman = np.exp(-delta_cost*k / temperature)
        # a i b
        if delta_cost > 0 or boltzman > random.random():
            ile_up += 1
            current_solution = new_solution
            current_cost = new_cost
            if new_cost < best_cost:
                best_solution = new_solution
                best_cost = new_cost

        #krok 4
        temperature = alpha(temperature)

    return best_solution, best_cost

