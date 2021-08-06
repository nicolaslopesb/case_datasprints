# Autor: Nicolas de Oliveira Lopes Braga - Case DataSprints

# Desenvolva um script em python para encontrar a média do petal_length de cada espécie presente no dataset.

# Import
import pandas as pd
import matplotlib.pyplot as plt

# Caminho URL da base de dados.
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

# Leitura do DataFrame.
use_columns = ['petal_length', 'species']

df_iris = pd.read_csv(url, usecols=use_columns)

# Consulta das médias por espécie.
df_iris = df_iris.groupby(['species']).mean().reset_index()
print(df_iris.head())

# Gráfico do DataFrame.
eixo_y = df_iris['petal_length']
eixo_x = ['Setosa', 'Versicolor', 'Virginica']

# Plotando gráfico simples.
plt.bar(eixo_x, eixo_y, color='blue', width=0.3)
plt.title('Average Iris Petal Length')
plt.xlabel('Species')
plt.ylabel('Mean Petal Length')

plt.show()