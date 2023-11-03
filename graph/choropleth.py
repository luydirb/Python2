#Importando as bibliotecas
import pandas as pd
import plotly.express as px
import requests

#Importando as configurações necessárias para gerar um mapa choropleth do Brasil
response = requests.get(url = 'https://raw.githubusercontent.com/fititnt/gis-dataset-brasil/master/uf/geojson/uf.json')
if response.status_code == 200:
    state_geo = response.json()
type(state_geo)

#Criando o dataframe
df = pd.DataFrame(pd.read_excel('brazil_covid19.xlsx',index_col=None,header=0))

#Filtrando o dataframe
df = df[(df['date'] <= '2020-12-31')]

#Agrupando as informações e pegando o maior número de cada índice
df = df.groupby(['cod'])['cases'].max()

#Configurando o gráfico choropleth
fig = px.choropleth_mapbox(df, geojson=state_geo, color="cases",
                    locations=df.index, featureidkey="properties.GEOCODIGO",
                    labels={'cases':'Casos de covid em 2020'},
                    mapbox_style="carto-positron",
                    color_continuous_scale=('reds'),
                    zoom=3, center = {"lat": -14.2350, "lon": -51.9253})

fig.update_geos(fitbounds="geojson", visible=True)
fig.update_layout(margin={"r":1,"t":0,"l":0,"b":0})

#Montando o gráfico
fig.show()