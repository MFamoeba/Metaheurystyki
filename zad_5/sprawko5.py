from matplotlib import pyplot as plt
from zad_5.fun.tools import swarm_generator
from zad_5.fun.testFunctionParameters import testFunctionParameters as tfp
from zad_5.algo.pso import pso



# warunki stopu, max liczba pokolen, tolerancja
max_iter = 500

# parametry algorytmu pso
# inercja(0,1) ->
# w - współczynnik innercji
# komponent poznawczy = (0,2) * przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze =
# c1 - współczynnik poznawczy
# komponent społeczny = (0,2) * przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze =
# c2 - współczynnik społeczny
# wielkosć populacji
w = 0.5
lolxd = [0.1, 0.3, 0.5, 0.7, 0.9]
c1 = 1
c2 = 1
#lolxd = [0.2, 0.6, 1, 1.4, 1.8]
pop_size = 320
#lolxd = [20, 80, 160, 320]
nr_of_runs = 10

funkcje_test1 = [tfp.SPHERE, tfp.GRIEWANK, tfp.ROSENBROCK]
#funkcje_test1 = [tfp.SPHERE]

history2 = []
for fun in funkcje_test1:
    print("Function {}".format(fun))
    name, objective_func, dim, lb, ub, accuracy = fun.value
    history2 = []
    for w in lolxd:
        history = []
        for i in range(nr_of_runs):
            swarm = swarm_generator(pop_size, lb, ub, dim)
            print("Progres {}%".format(i*100/nr_of_runs))
            history.append(pso(swarm, objective_func, w, c1, c2, max_iter))
        srednie = [sum(kolumna) / nr_of_runs for kolumna in zip(*history)]
        history2.append(srednie)
    x = numbers_list = [i for i in range(0, max_iter+1)]
    for i in range(len(lolxd)):
        y = history2[i]
        delta = lolxd[i]
        plt.plot(x, y, label='w = ' + str(delta))
    plt.title("PSO do "+ name + "\n" + "c1 = " + str(c1) + " pop_size = " + str(pop_size) + " c2 = " + str(c2))
    plt.yscale('log')
    plt.legend()
    plt.show()
