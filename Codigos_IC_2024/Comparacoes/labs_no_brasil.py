# -*- coding: utf-8 -*-
"""LABS no Brasil.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gkbb6AC87Qdh7XXIHyYGY4d-1hHvRhNa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#carregando arquivos do PC
from google.colab import files
uploaded = files.upload()

lab = pd.read_excel('LABS.xlsx')

lab.head(28)

cidades = lab['CIDADES']
qtd_ciencias = lab['QTD LABORATORIO CIENCIAS']
qtd_informatica = lab['QTD LABORATORIO INFORMATICA']

largura_barra = 0.35
indices = np.arange(len(cidades))

plt.bar(indices, qtd_ciencias, largura_barra, label='Laboratório Ciências')
plt.bar(indices + largura_barra, qtd_informatica, largura_barra, label='Laboratório Informática')

plt.xlabel('QTD DE LABS')
plt.ylabel('Cidades')
plt.title('Quantidade de Laboratórios de Ciências e Informática por Estado')
plt.xticks(indices + largura_barra / 2, cidades, rotation=45)  # Rótulos no eixo x (com rotação para melhor legibilidade)
plt.legend(fontsize=16)

plt.tight_layout()
plt.show()

