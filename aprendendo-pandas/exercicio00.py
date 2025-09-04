# Verificar tempos;
# Ordenação de maior a menor e na ordem inversa;
# Verificar estabilidade do algoritmo escolhido.
import time
import pandas as pd

dados = pd.read_csv('ai_assistant_usage_student_life.csv')

for x in dados:
  print(dados)


start1 = time.time()
df = pd.DataFrame(dados)
df.sort_values(['SatisfactionRating'], ascending=[False])
end1 = time.time()
print("Tempo de execução do algoritmo de ordenação (menor para maior): ", end1 - start1)
# print(df)
df

start2 = time.time()
# df = pd.DataFrame(dados)
df.sort_values(['SatisfactionRating'], ascending=[False], inplace=True)
end2 = time.time()
print("tempo de execução: ", end2 - start2)
# print(df)
df

df['SessionDate'] =pd.to_datetime(df['SessionDate'])
print("Ordenado por data, do mais recente para o mais antigo.")
df.sort_values(['SessionDate'], ascending=[False]) #inplace=True altera os dados no dataframe original


disciplina = dados['Discipline']
print("unicos: ", disciplina.unique())
print("quantidade: ", disciplina.nunique())

