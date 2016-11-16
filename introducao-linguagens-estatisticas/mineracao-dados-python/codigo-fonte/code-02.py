# -*- coding: utf-8 -*-
# code-02.py
"""
Dependência: biblioteca NumPy
Executar no prompt: pip install numpy

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo iris.csv

"""
# parte 1
import numpy as np
# lê as primeiras 4 colunas
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

# parte 2
print(data.shape)
# Saída: (150, 4)
print(target_names.shape)
# Saída: (150,)
# constrói uma coleção contendo elementos únicos
print(set(target_names))
# Saída python 2: set(['setosa', 'versicolor', 'virginica'])
# Saída python 3: {'virginica', 'versicolor', 'setosa'}
