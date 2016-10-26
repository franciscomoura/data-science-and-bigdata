# -*- coding: utf-8 -*-
# code-06.py
"""
Dependência: Matplotlib, NumPy
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy
Executar no prompt: pip install scikit-learn
Executar no prompt: pip install scipy

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo iris.csv

"""

import numpy as np

# lê as primeiras 4 colunas
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

# converter o vetor de strings que contêm a classe em números inteiros
target = np.zeros(len(target_names), dtype=np.int)
target[target_names == 'setosa'] = 0
target[target_names == 'versicolor'] = 1
target[target_names == 'virginica'] = 2

# parte 1
from sklearn.cluster import KMeans

# inicialização correta para o cluster mostrar o mesmo resultado a cada execução
kmeans = KMeans(n_clusters=3, init="k-means++", random_state=3425)
kmeans.fit(data)

# parte 2
clusters = kmeans.predict(data)

# parte 3
print("Completude e homogeneidade:")
from sklearn.metrics import completeness_score, homogeneity_score

print(completeness_score(target, clusters))
# Saída: 0.764986151449
print(homogeneity_score(target, clusters))
# Saída: 0.751485402199

# parte 4 - revisada
print("Gera o gráfico de dispersão")
import pylab as pl

pl.figure()

pl.subplot(211)  # topo, figura com as classes reais
pl.plot(data[target == 0, 2], data[target == 0, 3], 'bo', alpha=.7)  # 0 setosa
pl.plot(data[target == 1, 2], data[target == 1, 3], 'ro', alpha=.7)  # 1 versicolor
pl.plot(data[target == 2, 2], data[target == 2, 3], 'go', alpha=.7)  # 2 virginica
pl.xlabel('Comprimento da petala - cm')
pl.ylabel('Largura da petala - cm')
pl.axis([0.5, 7, 0, 3])

pl.subplot(212)  # embaixo, figura com as classes atribuídas automaticamente
pl.plot(data[clusters == 0, 2], data[clusters == 0, 3], 'go', alpha=.7)  # clusters 0 verginica
pl.plot(data[clusters == 1, 2], data[clusters == 1, 3], 'bo', alpha=.7)  # clusters 1 setosa
pl.plot(data[clusters == 2, 2], data[clusters == 2, 3], 'ro', alpha=.7)  # clusters 2 versicolor

pl.xlabel('Comprimento da petala - cm')
pl.ylabel('Largura da petala - cm')
pl.axis([0.5, 7, 0, 3])

pl.show()
