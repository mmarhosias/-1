import pandas as pd

df = pd.read_csv('p4_data_08.csv')
# 1. Количество продуктов по категориям
print("Количество продуктов по категориям:")
print(df['Category'].value_counts())

# 2. Суммарный объем поставок по категориям
print("\nСуммарный объем поставок по категориям:")
print(df.groupby('Category')['Volume'].sum())

# 3. Общий объем поставок
print(f"\nОбщий объем поставок: {df['Volume'].sum()}")

# 4. Количество просроченных продуктов
expired = df[df['Expired'] == True].shape[0]
print(f"\nКоличество просроченных продуктов: {expired}")