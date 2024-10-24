from enum import Enum
import zad_5.fun.test_functions as ts


class testFunctionParameters(Enum):
    HELP = ("Name","test_function", "dimensions", "lower_bound", "upper_bound", "accuracy")
    SPHERE = ("Funkcja sfery",ts.sphere_func, 20, -100, 100, 1e-4)
    F2 = ("Funkcja F2",ts.f2_function, 20, -100, 100, 1e-4)
    ROSENBROCK = ("Funkcja Rosenbrocka",ts.rosenbrock_function, 20, -2.048, 2.048, 30)
    GRIEWANK = ("Funkcja Griewanka",ts.griewank_function, 20, -600, 600, 0.1)
    ACKLEY = ("Funkcja Ackleya",ts.ackley_function, 20, -32, 32, 1e-4)
    BROWN = ("Funkcja Browna",ts.brown_function, 20, -1, 4, 1e-3)
    ZAKHAROV = ("Funkcja Zakharowa",ts.zakharov_function, 20, -10, 10, 1e-3)
    SCHEFFER = ("Funkcja Scheffera",ts.scheffer_function, 20, -100, 100, 1e-3)
    RASTGRIN = ("Funkcja Rastgrin",ts.rastgrin_function, 20, -5.12, 5.12, 1e-3)
    EXAMPLE1 = ("Przykład 1",ts.example_1,1, -150, 150, 1e-3)
    EXAMPLE2 = ("Przykład 2", ts.example_2, 2, -15, 15, 1e-3)
