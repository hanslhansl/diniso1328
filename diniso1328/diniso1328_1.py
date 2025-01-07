import math as m
from diniso1328 import FlankToleranceClass


def f_Hbeta(d : float, b : float, A : FlankToleranceClass):
    return (0.07 * m.sqrt(d) + 0.45 * m.sqrt(b) + 4) * m.pow(m.sqrt(2), A - 5)

