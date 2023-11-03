#Importando as bibliotecas
import pandas as pd
import plotly.express as px

#Criando o dataframe
df = pd.DataFrame(pd.read_excel('brazil_covid19.xlsx',index_col=None,header=0))

#Filtrando o dataframe
df = df[(df['date'] <= '2020-12-31') & (df['region'] == 'Sul')]

#Agrupando as informações e pegando o maior número de cada índice
df = df.groupby(['state'])['cases'].max()

#Configurando o gráfico de setores
fig = px.pie(df, values='cases', names=df.index, title='Porcentagem de casos de covid na região Sul por estado')

#Montando o gráfico
fig.show()