from time import *


import pandas as pd
import numpy as np
start = time()
df = pd.read_csv('testing_data.txt')
print(time() - start)

# # Iterrows
# start3 = time()
# total = []
# for index, row in df.iterrows():
#     total.append(row['src_bytes'] + row['dst_bytes'])
# # print(total)
# print('start3', time() - start3, 'Iterrows')


# # For loop
# start4 = time()
# total = []
# for index in range(len(df)):
#     # print(df['src_bytes'].loc[index])
#     total.append(df['src_bytes'].loc[index] + df['dst_bytes'].loc[index])
# # print(total)
# print('start4', time() - start4, 'For loop')


# # Apply
# start5 = time()
# df.apply(lambda row: row['src_bytes'] + row['dst_bytes'], axis=1).to_list()
# print('start5', time() - start5, 'Apply')


# Itertuples
start2 = time()
total = []
for row in df.itertuples():
    total.append(row[5] + row[6])
print('start2', time() - start2, 'Itertuples')


# Генерация списка
start6 = time()
l = [src + dst for src, dst in zip(df['src_bytes'], df['dst_bytes'])]
# print(l)
print('start6', time() - start6, 'Генерация списка')


# Векторизация Pandas
start7 = time()
(df['src_bytes'] + df['dst_bytes']).to_list()
print('start7', time() - start7, 'Векторизация Pandas')


# Векторизация NumPy
start1 = time()
(df['src_bytes'].to_numpy() + df['dst_bytes'].to_numpy()).tolist()
print('start1', time() - start1, 'Векторизация NumPy')