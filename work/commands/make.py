import pandas as pd

# Загрузка файла
df = pd.read_csv('all.csv')

# Замена всех символы переноса строки на экранированный вариант
df = df.replace({"\n": "<NEWLINE>"}, regex=True)

# Сохранение обновленного файла
df.to_csv('test_modified.csv', index=False)