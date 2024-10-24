# -*- coding: utf-8 -*-
"""RO - Escolas Rurais.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qdusEgTeOfA0rGGzhjHZLYW8uknPeTOn
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
estado = gpd.read_file('RO_Municipios_2022.zip')

estado.head()

estado.plot()

#carregando arquivos do PC
from google.colab import files
uploaded = files.upload()

rural = pd.read_excel('Escola rural no Brasil.xlsx')
rural.head()

#criando um simples mapa no folium
def criar_mapa():
  fmap = folium.Map(location=[0.0, 0.0], tiles="OpenStreetMap", zoom_start=2)
  return fmap

#juntando os dados em um novo dataframe
rural_por_cidade = pd.merge(estado,rural,left_on='NM_MUN',right_on='CIDADE',how='left',sort=True)
rural_por_cidade.head()

#criando a coluna do percentual de labs de ciencias por cidade
rural_por_cidade['percentual_rural'] = rural_por_cidade['QTD']/1

# Mapa coropletico com o percentual de escolas rurais por cidade
def plot_coropletico(fmap):
    choropleth_labs = folium.Choropleth(
        geo_data=rural_por_cidade,
        data=rural_por_cidade,
        columns=['NM_MUN', 'percentual_rural'],
        key_on='feature.properties.NM_MUN',  # Modify this line based on your GeoDataFrame structure
        legend_name='QUANTIDADE DE ESCOLAS RURAIS POR CIDADE',
        fill_color='YlGnBu',
    ).add_to(fmap)

    choropleth_labs.geojson.add_child(
        folium.features.GeoJsonTooltip(['NM_MUN', 'percentual_rural'])
    )
    return fmap

mapa = criar_mapa()

plot_coropletico(mapa)

