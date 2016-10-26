# -*- coding: utf-8 -*-
# code-03.py
"""
Dependência: Matplotlib, NumPy
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo iris.csv

"""

import numpy as np

# lê as primeiras 4 colunas
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

"""
***EXCLUIR ESTE CÓDIGO******
import pylab as pl
pl.plot(data[target_names == 'setosa', 0], 
        data[target_names == 'setosa', 2], 'bo')
pl.plot(data[target_names == 'versicolor',0], 
        data[target_names == 'versicolor',2], 'ro')
pl.plot(data[target_names == 'virginica', 0], 
        data[target_names == 'virginica', 2], 'go')
pl.show()
"""

"""
# comprimento x largura da sepala
import pylab as pl
pl.plot(data[target_names == 'setosa', 0], data[target_names == 'setosa', 1], 'bo')
pl.plot(data[target_names == 'versicolor',0], data[target_names == 'versicolor',1], 'ro')
pl.plot(data[target_names == 'virginica', 0], data[target_names == 'virginica', 1], 'go')
pl.ylabel('Largura da sepala - cm')
pl.xlabel('Comprimento da sepala - cm')
pl.show()
"""

# comprimento e largura da petala
import pylab as pl

pl.plot(data[target_names == 'setosa', 2], data[target_names == 'setosa', 3], 'bo')
pl.plot(data[target_names == 'versicolor', 2], data[target_names == 'versicolor', 3], 'ro')
pl.plot(data[target_names == 'virginica', 2], data[target_names == 'virginica', 3], 'go')
pl.ylabel('Largura da petala - cm')
pl.xlabel('Comprimento da petala - cm')
pl.axis([0.5, 7, 0, 3])
pl.show()
