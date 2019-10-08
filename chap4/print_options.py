# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:56:32 2016

@author: Francisco Bustamante
"""

import numpy as np
a = np.linspace(3, 19, 7)
print(a)

np.set_printoptions(precision=2)
b = np.linspace(3, 19, 7)
print("\n", b)

np.set_printoptions(formatter={'float': lambda x: format(x, '6.2e')})
c = np.linspace(3, 19, 7)
print("\n", c)

np.set_printoptions(formatter={'float': lambda x: format(x, '6.3f')})
d = np.linspace(3, 19, 7)
print("\n", d)

np.set_printoptions(precision=8)
e = np.linspace(3, 19, 7)
print("\n", e)
