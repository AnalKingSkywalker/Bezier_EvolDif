import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

#Curva de bezier

def bezier_curve(control_points, n_points=1000):
    n = len(control_points) - 1
    t = np.linspace(0, 1, n_points)
    curve = np.zeros((n_points, 2))
    
    for i, (px, py) in enumerate(control_points):
        bernstein_poly = comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        curve[:, 0] += bernstein_poly * px
        curve[:, 1] += bernstein_poly * py
    
    return curve