#%%
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
# %%
data = pd.read_csv('Hitters.csv')
print(f"Número de observações: {data.shape[0]}")
# %%
data.dropna(subset=['Salary'], inplace=True)
print(f"Número de observações após a limpeza: {data.shape[0]}")
# %% Criando nossa própria Decision Tree
X = data[['Years', 'Hits']]
y = data['Salary']

#%% Exemplo de construção da árvore de decisão

df = pd.DataFrame()
df['X1'] = [1,2,3,4,5]
df['X2'] = [4,6,8,10,12]
df['Y'] = [0,5,10,15,20]

X = df[['X1', 'X2']]
y = df['Y']

def calculate_rss_division(X, y, var, s):
    if len(X)<=2:
        print('Não é possível dividir o dataset em dois grupos')
        return y.mean()
    
    rss_r1 = np.sum((y[X[var] <= s] - np.mean(y[X[var] <= s]))**2)
    rss_r2 = np.sum((y[X[var] > s] - np.mean(y[X[var] > s]))**2)
    rss_total = rss_r1 + rss_r2
    return rss_total
#%% 1 - Primeira iteração
print(calculate_rss_division(X, y, 'X1', 1.5))
print(calculate_rss_division(X, y, 'X1', 2.5))
print(calculate_rss_division(X, y, 'X1', 3.5))
print(calculate_rss_division(X, y, 'X1', 4.5))

print(calculate_rss_division(X, y, 'X2', 5))
print(calculate_rss_division(X, y, 'X2', 7))
print(calculate_rss_division(X, y, 'X2', 9))
print(calculate_rss_division(X, y, 'X2', 11))
    
#%% 2 - Segunda iteração
melhor_resultado = ('X2',7)

R1_X = X[X['X2'] <= 7]
R1_y = y[X['X2'] <= 7]

R2_X = X[X['X2'] > 7]
R2_y = y[X['X2'] > 7]

print(calculate_rss_division(R1_X, R1_y, 'X1', 1.5))

# %%
