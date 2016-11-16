# -*- coding: utf-8 -*-
# code-09.py
"""
Dependência: Matplotlib, NumPy, scikit-learn
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy
Executar no prompt: pip install scikit-learn
Executar no prompt: pip install scipy

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo iris.csv

"""

import numpy as np
# lê as primeiras 4 colunas
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

# parte 1
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

# parte 2
pcad = pca.fit_transform(data)

# parte 3
import pylab as pl
pl.plot(pcad[target_names == 'setosa', 0], pcad[target_names == 'setosa', 1], 'bo')
pl.plot(pcad[target_names == 'versicolor', 0], pcad[target_names == 'versicolor', 1], 'ro')
pl.plot(pcad[target_names == 'virginica', 0], pcad[target_names == 'virginica', 1], 'go')
pl.show()

# parte 4
print("Variância: ")
print(pca.explained_variance_ratio_)
# Saída: [ 0.92461621  0.05301557]

# parte 5
print("Perda de informação: ")
print(1-sum(pca.explained_variance_ratio_))
# Saída: 0.0223682249752

# parte 6
data_inv = pca.inverse_transform(pcad)

# parte 7
print("Resultado inverso:")
print(abs(sum(sum(data - data_inv))))

# parte 8
print("Preservação da informação: ")
for i in range(1, 5):
    pca = PCA(n_components=i)
    pca.fit(data)
    print("{0:1d} {1:11} = {2:.5f}%".format(i, 
                                  "componente" if i == 1 else "componentes", 
                                  sum(pca.explained_variance_ratio_) * 100))






