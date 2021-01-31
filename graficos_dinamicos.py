"""
    - Script para gerar gráficos dinâmicos
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.interpolation import shift
from random import random

t = np.arange(0, 5, 1)
temp = np.random.randn(5) + 25

plt.ion()
plt.style.use('ggplot')

for i in range(10):
    t += 1  # [0, 1, 2, 3, 4] +1 = [1, 2, 3, 4, 5]

    new_temp = (random() + 4 - 2) + 25

    temp = shift(temp, -1, cval=new_temp)  # [25, 24, 23, 26, 27] >> [24, ]

    print(t)
    print(temp)

    plt.cla()
    plt.clf()
    plt.bar(t, temp)
    plt.title('Temperatura Ambiente (°C)')
    plt.xlabel('Tempo')
    plt.ylim(0, 30)
    plt.pause(1)

plt.ioff()
plt.show()
