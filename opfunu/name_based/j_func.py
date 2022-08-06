#!/usr/bin/env python
# Created by "Thieu" at 17:30, 30/07/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%


import numpy as np
from opfunu.benchmark import Benchmark

class JennrichSampson(Benchmark):
    """
   [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
   
        name=" Jennrich Sampson "
       latex_formula = r'f_{\text{JennrichSampson}}(x) = \sum_{i=1}^{10} \left [2 + 2i
        - (e^{ix_1} + e^{ix_2}) \right ]^2
       latex_formula_dimension = r'd \in 2'   # two dimentions
       latex_formula_bounds = r'x_i \in [-1, 1], \forall i \in \llbracket 1, d\rrbracket'
       latex_formula_global_optimum = r'f(x) = 124.3621824` for x \in \llbracket 0.257825, 0.257825\rrbracket'
  
    continuous = True
    linear = False
    convex = True
    unimodal = False
    separable = True

    differentiable = True
    scalable = True
    randomized_term = False
    parametric = False

    modality = False  # Number of ambiguous peaks, unknown # peaks


    def __init__(self, ndim=None, bounds=None):
        Super().__init__()
        
        self.dim_changeable = True
        self.dim_default = 2
        self.check_ndim_and_bounds(ndim, bounds, np.array([[-1., 1.] for _ in range(self.dim_default)]))
        self.f_global = 124.3621824.
        
        self._bounds = list(zip([(-1.0] * self.N, [1.0] * self.N))
        self.x_global = 0.257825 * np.zeros(self.ndim)
      
      

    def evaluate(self, x, *args):
        self.nfev += 1

        i = arange(1, 11)
        return np.sum((2 + 2 * i - (np.exp(i * x[0]) + np.exp(i * x[1]))) ** 2)


class Judge(Benchmark):
    
    """
    [1] Gavana, A. Global Optimization Benchmarks and AMPGO retrieved 2015
    """
    name =" Judge objective function "
    
    
    latex_formula = r'f_{\text{Judge}}(x) = \sum_{i=1}^{20}
        \left [ \left (x_1 + A_i x_2 + B x_2^2 \right ) - C_i \right ]^2
    Where, in this exercise:
    .. math::
        \begin{cases}
        C = [4.284, 4.149, 3.877, 0.533, 2.211, 2.389, 2.145,
        3.231, 1.998, 1.379, 2.106, 1.428, 1.011, 2.179, 2.858, 1.388, 1.651,
        1.593, 1.046, 2.152] \\
        A = [0.286, 0.973, 0.384, 0.276, 0.973, 0.543, 0.957, 0.948, 0.543,
             0.797, 0.936, 0.889, 0.006, 0.828, 0.399, 0.617, 0.939, 0.784,
             0.072, 0.889] \\
        B = [0.645, 0.585, 0.310, 0.058, 0.455, 0.779, 0.259, 0.202, 0.028,
             0.099, 0.142, 0.296, 0.175, 0.180, 0.842, 0.039, 0.103, 0.620,
             0.158, 0.704]
        \end{cases}
        latex_formula_dimension = r'd \in 2'   # two dimentions
        latex_formula_bounds = r'x_i \in [-10, 10], \forall i \in \llbracket 1, 2\rrbracket
        latex_formula_global_optimum = r`f(x_i) = 16.0817307` for bf{x} \in \llbracket 0.86479, 1.2357\rrbracket'
        continuous = True
        linear = False
        convex = True
        unimodal = False
        separable = True

        differentiable = True
        scalable = True
        randomized_term = False
        parametric = False

        modality = False  # Number of ambiguous peaks, unknown # peaks
    

    def __init__(self, ndim=None, bounds=None):
        Super().__init__()
        
        self.dim_changeable = True
        self.dim_default = 2
        self.check_ndim_and_bounds(ndim, bounds, np.array([[-10, 10] for _ in range(self.dim_default)]))
        self.f_global = 16.0817307
        self.x_global = [0.86479, 1.2357]  * np.zeros(self.ndim)

        self.c = asarray([4.284, 4.149, 3.877, 0.533, 2.211, 2.389, 2.145,
                          3.231, 1.998, 1.379, 2.106, 1.428, 1.011, 2.179,
                          2.858, 1.388, 1.651, 1.593, 1.046, 2.152])

        self.a = asarray([0.286, 0.973, 0.384, 0.276, 0.973, 0.543, 0.957,
                          0.948, 0.543, 0.797, 0.936, 0.889, 0.006, 0.828,
                          0.399, 0.617, 0.939, 0.784, 0.072, 0.889])

        self.b = asarray([0.645, 0.585, 0.310, 0.058, 0.455, 0.779, 0.259,
                          0.202, 0.028, 0.099, 0.142, 0.296, 0.175, 0.180,
                          0.842, 0.039, 0.103, 0.620, 0.158, 0.704])

    def evaluate(self, x, *args):
        self.check_solution(x)
        self.nfev += 1

        return np.sum(((x[0] + x[1] * self.a + (x[1] ** 2.0) * self.b) - self.c)
                    ** 2.0)