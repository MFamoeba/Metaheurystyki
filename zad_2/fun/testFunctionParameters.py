from enum import Enum
import zad_2.fun.test_functions as ts


class testFunctionParameters(Enum):
    HELP = ("Name","test_function", "dimensions", "lower_bound", "upper_bound", "temp_start", "alpha", "k", "max_iter")
    EXAMPLE1 = ("Przykład 1",ts.example_1, 1, [-150], [150], 500, ts.alfa_1, 0.1, 3000)
    EXAMPLE2 = ("Przykład 2", ts.example_2, 2, [-15, -15], [15,15], 90, ts.alfa_1, 0.5, 200)
    EXAMPLE4 = ("Przykład 4", ts.example_4, 1, [-1], [2], 5, ts.alfa_4, 0.1, 1200)
    EXAMPLE5 = ("Przykład 5", ts.example_5, 2, [-3,4.1], [12, 5.8], 100, ts.alfa_1, 0.2, 3000)
