# -*- coding: utf-8 -*-
# code-04.py
"""
Dependência: Matplotlib, NumPy
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo iris.csv

"""

import numpy as np

# lê as primeiras 4 colunas
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)


import pylab as pl
xmin = min(data[:, 0])
xmax = max(data[:, 0])
pl.figure()
pl.subplot(411) # distribuição da classe setosa (primeira, no topo)
pl.hist(data[target_names == 'setosa', 0], color='b', alpha=.7)
pl.xlim(xmin, xmax)
pl.xlabel('Comprimento da sepala - cm')
pl.ylabel('Ocorrencias')

pl.subplot(412) # distribuição da classe setosa versicolor class (segunda)
pl.hist(data[target_names == 'versicolor', 0], color='r', alpha=.7)
pl.xlim(xmin, xmax)
pl.xlabel('Comprimento da sepala - cm')
pl.ylabel('Ocorrencias')

pl.subplot(413) # distribuição da classe setosa virginica class (terceira)
pl.hist(data[target_names == 'virginica', 0], color='g', alpha=.7)
pl.xlim(xmin, xmax)
pl.xlabel('Comprimento da sepala - cm')
pl.ylabel('Ocorrencias')

pl.subplot(414) # histograma global (quarto, último)
pl.hist(data[:, 0], color='y', alpha=.7)
pl.xlim(xmin, xmax)
pl.xlabel('Comprimento da sepala - cm')
pl.ylabel('Ocorrencias')

pl.show()
