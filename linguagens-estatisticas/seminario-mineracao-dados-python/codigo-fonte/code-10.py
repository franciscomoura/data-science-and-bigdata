# -*- coding: utf-8 -*-
# code-10.py
"""
Dependência: Matplotlib, NumPy, NetworkX
Executar no prompt: pip install matplotlib
Executar no prompt: pip install numpy
Executar no prompt: pip install scipy
Executar no prompt: pip install networkx

*** Atenção:
Este arquivo deverá executado no mesmo diretório do arquivo lesmiserables.gml

"""
# parte 1
import networkx as nx
import matplotlib.pyplot as plt
G = nx.read_gml('lesmiserables.gml') # lê o arquivo gml
nx.draw_networkx(G, alpha = 0.5, font_size = 10) # desenha a rede
plt.show() # plota em tela o gráfico da rede

# parte 2
import numpy as np
deg = nx.degree(G)
values = list(deg.values())
print(np.min(values))
print(np.percentile(values, 25)) # calcula o primeiro quartil
print(np.median(values))
print(np.percentile(values, 75)) # calcula o terceiro quartil
print(np.max(values))

# parte 3
Gt = G.copy()
dn = nx.degree(Gt)
for n in Gt.nodes():
    if dn[n] <= 10:
        Gt.remove_node(n)
nx.draw_networkx(Gt, alpha = 0.5, font_size = 10) # desenha a rede
plt.show()

# parte 4
# from networkx import find_cliques
cliques = list(nx.find_cliques(G))
print(max(cliques, key=lambda l: len(l)))

