import pandas as pd

df = pd.read_csv('data.csv', names=['CARD', 'PORT', 'USER'])

ports = df['PORT'].unique().tolist()

for port in ports:
    print(port, df['USER'][df['PORT'] == port].count())
