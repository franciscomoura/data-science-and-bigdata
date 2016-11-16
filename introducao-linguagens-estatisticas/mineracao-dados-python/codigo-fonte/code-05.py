# -*- coding: utf-8 -*-
# code-05.py
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

# converter o vetor de strings que contêm a classe em números inteiros
target = np.zeros(len(target_names), dtype=np.int)
target[target_names == 'setosa'] = 0
target[target_names == 'versicolor'] = 1
target[target_names == 'virginica'] = 2

# Classificação pelo método Guassian naives Bayes
print("Classificação: ")
from sklearn.naive_bayes import GaussianNB
# instanciar e treinar o classificador
classifier = GaussianNB()
# treinar no conjunto de dados iris
classifier.fit(data, target)

# Classificação pelo métdo de predição
print (classifier.predict(data[0].reshape(1, -1)))
# Saída: [1]
print (target[0])
# Saída: 1

# dividir o conjunto de dados em amostras de treinamento e teste
print("Índice de precisão do classificador:")
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.4, random_state=0)
# treinar o classificador com os conjuntos de treino específicos
classifier.fit(data_train, target_train) # treino
print (classifier.score(data_test, target_test)) # teste
# Saída: 0.93333333333333335

# matriz de confusão
print("Matriz de confusão:")
from sklearn.metrics import confusion_matrix
print (confusion_matrix(classifier.predict(data_test),target_test))
""" Saída:
     [[16 0 0]
     [ 0 23 4]
     [ 0 0 17]]
"""

# relatório de classificação
print("Relatório de classificação:")
from sklearn.metrics import classification_report
print (classification_report(classifier.predict(data_test), 
    target_test, target_names=['setosa', 'versicolor', 'virginica']))

# Cross validation
print("Validação cruzada: ")
from sklearn.model_selection import cross_val_score
# cross validation com 6 iterações 
scores = cross_val_score(classifier, data, target, cv=6)
print(scores)
# Saída: [ 0.92592593  1.     0.91666667  0.91666667  0.95833333  1.   ]

# precisão média
print("Precisão média:")
print(np.mean(scores))
# Saída: 0.952932098765

