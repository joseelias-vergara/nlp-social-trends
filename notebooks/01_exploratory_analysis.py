from datasets import load_dataset
import pandas as pd

meses = ["2024-10", "2024-11", "2024-12", "2025-01", "2025-02"]

dfs = []
for mes in meses:
    dataset = load_dataset("RealTimeData/bbc_news_alltime", mes)
    df_mes = dataset['train'].to_pandas()
    dfs.append(df_mes)

df = pd.concat(dfs, ignore_index=True)

print(df.head())
print(df.shape)

print(df['section'].value_counts())
# Fechas
print(df['published_date'].min())
print(df['published_date'].max()) 

# Nulos
print(df.isnull().sum())