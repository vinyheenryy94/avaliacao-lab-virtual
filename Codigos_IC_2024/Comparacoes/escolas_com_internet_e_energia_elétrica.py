# -*- coding: utf-8 -*-
"""Escolas com internet e energia elétrica

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nFdy13eK2pskU95ImQfLt5gJM6wysT3Q
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#carregando arquivos do PC
from google.colab import files
uploaded = files.upload()

escola = pd.read_excel('Internet_Energia.xlsx')
escola.head()

estados = escola['ESTADOS']
internet = escola['INTERNET']
energia = escola['ENERGIA']

largura_barra = 0.45
indices = np.arange(len(estados))

plt.bar(indices, internet, largura_barra, label='Escolas com Internet')
plt.bar(indices + largura_barra, energia, largura_barra, label='Escolas com energia')

plt.xlabel('ESTADOS')
plt.ylabel('QTD ESCOLAS')
plt.title('Comparativo de Escolas com Internet e Energia')
plt.xticks(indices + largura_barra / 2, estados, rotation=45)  # Rótulos no eixo x (com rotação para melhor legibilidade)
plt.legend(fontsize=16)

plt.tight_layout()
plt.show()

