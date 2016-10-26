# -*- coding: utf-8 -*-
# code-01.py
"""
O arquivo iris.csv será gravado no mesmo diretório do arquivo-fonte
"""

print("Iniciando importação do arquivo csv iris...")
"""
Workarround para executar em ambiente python 2 e python 3
"""
try:
    import urllib.request as url_lib
except ImportError:
    import urllib2 as url_lib

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
remote_file = url_lib.urlopen(url)
with open('iris.csv', 'wb') as local_file:
    local_file.write(remote_file.read())
local_file.close()
print("Concluída importação do arquivo csv iris!")
