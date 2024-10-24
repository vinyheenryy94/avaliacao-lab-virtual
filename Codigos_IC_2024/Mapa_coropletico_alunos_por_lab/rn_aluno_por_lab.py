# -*- coding: utf-8 -*-
"""RN - Aluno por Lab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fogCyd2luDTznW7LtDPfDtripGAxBKI3
"""

#visualização de dados
import seaborn as sns
#ciência de dados
import pandas as pd
#mapas e geolocalização
import geopandas as gpd
import folium
#manipulação de arquivos json
import json

#carregando arquivos do PC
from google.colab import files
uploaded = files.upload()

#carregando o arquivo com o formato das cidades
import geopandas as gpd
estado = gpd.read_file('RN_Municipios_2022.zip')

estado.head()

estado.plot()

#carregando arquivos do PC
from google.colab import files
uploaded = files.upload()

#visualização de dados
import seaborn as sns
#ciência de dados
import pandas as pd
#mapas e geolocalização
import geopandas as gpd
import folium
#manipulação de arquivos json
import json

propor = pd.read_excel('Alunos matriculados.xlsx')
propor.head(30)

#criando um simples mapa no folium
def criar_mapa():
  fmap = folium.Map(location=[-14.235, -51.9253], tiles="OpenStreetMap", zoom_start=4)
  return fmap

#juntando os dados em um novo dataframe
aluno_por_lab = pd.merge(estado,propor,left_on='NM_MUN',right_on='CIDADES',how='left',sort=True)
aluno_por_lab.head()

# substituindo valores NaN por 0 nas colunas 'QTD ALUNOS' e 'LAB' usando um loop
for index, row in aluno_por_lab.iterrows():
    if pd.isnull(row['QTD ALUNOS']):
        aluno_por_lab.at[index, 'QTD ALUNOS'] = 0
    if pd.isnull(row['LAB']):
        aluno_por_lab.at[index, 'LAB'] = 0

#criando a coluna da proporção de laboratorios por aluno
aluno_por_lab['percentual_lab'] = aluno_por_lab['QTD ALUNOS']/aluno_por_lab['LAB']

aluno_por_lab.head()

# Mapa coropletico com o percentual de lab por alunos
def plot_coropletico(fmap):
    choropleth_labs = folium.Choropleth(
        geo_data=aluno_por_lab,
        data=aluno_por_lab,
        columns=['NM_MUN', 'percentual_lab'],
        key_on='feature.properties.NM_MUN',  # Modify this line based on your GeoDataFrame structure
        legend_name='QUANTIDADE DE ALUNO POR LABORATÓRIO DE INFORMÁTICA',
        fill_color='YlGnBu',
        highlight=True,
        line_opacity=0.5,
        line_weight=1,
        fill_opacity=0.7,
        range=[0, 100]
    ).add_to(fmap)

    choropleth_labs.geojson.add_child(
        folium.features.GeoJsonTooltip(['NM_MUN', 'percentual_lab'])
    )
    return fmap

mapa = criar_mapa()

# substituindo valores NaN por 0 nas colunas 'QTD ALUNOS' e 'LAB' usando um loop e substituindo o percentual lab por 0 ao inves de inf
import numpy as np
for index, row in aluno_por_lab.iterrows():
    if pd.isnull(row['percentual_lab']):
        aluno_por_lab.at[index, 'percentual_lab'] = 0
    if row['percentual_lab'] == np.inf:
        aluno_por_lab.at[index, 'percentual_lab'] = 0

aluno_por_lab

plot_coropletico(mapa)

