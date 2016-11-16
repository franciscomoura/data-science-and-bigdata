# -*- coding: utf-8 -*-
# code-07.py
"""
Dependência: Matplotlib, NumPy
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy
Executar no prompt: pip install scikit-learn
Executar no prompt: pip install scipy

"""
# parte 1
import numpy as np
x = np.random.rand(40,1) # variável explicativa
y = x*x*x+np.random.rand(40,1)/5 # variável dependente

# parte 2
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(x,y)

# parte 3
import pylab as pl
xx = np.linspace(0,1,40)
pl.plot(x, y, 'o', xx, linreg.predict(np.matrix(xx).T),'--r')
pl.show()

# parte 4
print("Erro médio quadrático: ")
from sklearn.metrics import mean_squared_error
print(mean_squared_error(linreg.predict(x),y))
# Saída: 0.0202788893782
