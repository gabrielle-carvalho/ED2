# Verificar tempos; Ordenação de maior a menor e na ordem inversa; Verificar estabilidade do algoritmo escolhido.
import time
import pandas as pd

dados = pd.read_csv("ai_assistant_usage_student_life.csv")

print("Visualização inicial dos dados:")
print(dados.head())

# for x in dados:
#   print(dados)

def ordenar_crescente(df):
  start = time.time()
  ordenado = df.sort_values(['SatisfactionRating'], ascending=[False])
  end = time.time()
  print("Tempo de execução do algoritmo de ordenação (menor para maior): ", end - start)
  return ordenado

def ordenar_decrescente(df):
  start = time.time()
  ordenado = df.sort_values(['SatisfactionRating'], ascending=False, kind="mergesort")
  end = time.time()
  print("tempo de execução: ", end - start)
  return ordenado

def ordenar_por_data(df):
  df = df.copy()
  df["SessionDate"] = pd.to_datetime(df["SessionDate"])
  ordenado = df.sort_values("SessionDate", ascending=False, kind="mergesort")
  print("Ordenado por data mais recente p/ mais antigo:")
  print(ordenado.head())
  return ordenado

def analisar_disciplina(df):
  disciplina = df['Discipline']
  print("unicos: ", disciplina.unique())
  print("quantidade: ", disciplina.nunique())


def main():
    df_cresc = ordenar_crescente(dados)
    df_desc = ordenar_decrescente(dados)
    df_data = ordenar_por_data(dados)

    analisar_disciplina(dados)

    print("\nTop 5 crescente:\n", df_cresc.head())
    print("\nTop 5 decrescente:\n", df_desc.head())


if __name__ == "__main__":
    main()