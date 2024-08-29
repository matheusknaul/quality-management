import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from range import Range

vi = [10, 20, 30, 40, 51]
vref = [11, 22, 30, 40, 50]
incerteza = [1, 2, 2, 2, 4]
    
faixa = Range(vref, vi, incerteza, False, 3, False)
