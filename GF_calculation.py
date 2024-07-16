import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import os


# from Green_function import Noninteracting
# from Green_function import spectra
import Green_function as Gf


Gf.spectra(Gf.Scalarss(), 'all' , omega=2 , kz = 1)

