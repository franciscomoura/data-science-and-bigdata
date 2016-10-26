# -*- coding: utf-8 -*-
# code-08.py
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
data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
# lê a quinta coluna(última)
target_names = np.genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

# parte 1
print("Coeficiente de correlação:")
corr = np.corrcoef(data.T) # T. dá a transposição
print(corr)


# parte 2
import pylab as pl
pl.pcolor(corr)
pl.colorbar() # adicionar barra de cores
# organiza os nomes das variáveis nos eixos cartesianos
pl.xticks(np.arange(0.5, 4.5), ['sepal length', 'sepal width', 'petal length', 'petal width'], fontsize=6)
pl.yticks(np.arange(0.5, 4.5), ['sepal length', 'sepal width', 'petal length', 'petal width'], fontsize=6)
pl.grid(True)
pl.title('Coeficiente de correlacao plantas Iris')
pl.show()
