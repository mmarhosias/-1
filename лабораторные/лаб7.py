import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('p4_data_08.csv')
plt.figure(figsize=(10, 5))
plt.hist(df['Volume'], bins=20, color='blue', alpha=0.7)
plt.title('Распределение объемов поставок')
plt.xlabel('Объем')
plt.ylabel('Частота')
plt.show()

df.boxplot(column='Volume', by='Category')
plt.title('Boxplot по категориям')
plt.show()