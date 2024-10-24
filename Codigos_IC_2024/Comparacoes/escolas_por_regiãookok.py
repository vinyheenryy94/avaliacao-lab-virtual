# -*- coding: utf-8 -*-
"""Escolas por RegiãoOKOK.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LkrYf-SDFv_O-i7_FPj17sRBBaFZcSPn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

escolas = pd.read_excel('escolas_regiao.xlsx')

escolas.head(5)

plt.figure(figsize=(8, 6))
plt.bar(escolas['Região'], escolas['Quantidade'])
plt.xlabel('Região')
plt.ylabel('Quantidade de escolas')
plt.title('Contagem de Escolas por Região')

estadual = pd.read_excel('estadual_regiao.xlsx')

estadual.head(5)

plt.figure(figsize=(8, 6))
plt.bar(estadual['Região'], estadual['Quantidade'])
plt.xlabel('Região')
plt.ylabel('Quantidade de escolas')
plt.title('Contagem de Escolas Estaduais por Região')

municipal = pd.read_excel('municipais_regiao.xlsx')

municipal.head(5)

plt.figure(figsize=(8, 6))
plt.bar(municipal['Região'], municipal['Quantidade'])
plt.xlabel('Região')
plt.ylabel('Quantidade de escolas')
plt.title('Contagem de Escolas Municipais por Região')

estmun = pd.read_excel('estadual_muncipal_regiao.xlsx')

estmun.head(5)

plt.figure(figsize=(8, 6))
plt.bar(estmun['Região'], estmun['Quantidade'])
plt.xlabel('Região')
plt.ylabel('Quantidade de escolas')
plt.title('Contagem de Escolas Estaduais e Municipais por Região')

