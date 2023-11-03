
#Importando bibliotecas
import pandas as pd
import plotly.express as px

#Criação do dataframe
df = pd.read_excel(r'brazil_covid19.xlsx',index_col=None,header=0)

#Filtrando o dataframe
df = df[(df['date'] <= '2020-12-31') & (df['region'] == 'Sul')]

#Configurando o gráfico de linhas
fig = px.line(df, x='date', y='deaths', color='state', title= 'Mortes por covid por dia na região Sul em 2020')

#Gerando o gráfico de linhas
fig.show()