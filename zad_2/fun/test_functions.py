import math
import numpy as np

def example_1(x):
    if -105 < x < -95:
        return -2 * abs(x+100) + 10
    elif 95 < x < 105:
        return -2.2 * abs(x-100) + 11
    else:
        return 0

def example_2(x1):
    x, y = x1
    a = 8*math.exp(-(x+12)**2-(y+12)**2)
    b = 9/(1+(x+12)**2+(y-12)**2)
    c = 20/((math.cosh(x-12))**2+math.cosh(y+12)**2)
    d = 176/((math.exp(x-12)+2+math.exp(-x+12))*(math.exp(y-12)+2+math.exp(-y+12)))
    return a + b + c + d

def example_4(x):
    return x*math.sin(10*x*math.pi)+1

def example_5(x1):
    x, y = x1
    return 21.5+x*math.sin(4*math.pi*x)+y*math.sin(20*math.pi*y)