#%%
import numpy as np
import statspy as sp
import seaborn as sns
# %%
'''
    Notas de teste
'''
array_of_scores = [3,3,5,6,5,4,2,1,4,7]

# %%
'''
    O que é a média?
        - Tendência central, concentração dos dados.
        
'''
mean = np.mean(array_of_scores)
print(f"Média: {mean}")
print(f"Se entrasse uma nova nota, provavelmente seria: {mean}")
# %%
'''
    O que é o desvio padrão?
        - Mostra o quanto os dados estão dispersos. 
            - Quanto maior, mais distante os dados são da média e, portanto, mais heterogêneos.
            - Quanto menor, mais próximos os dados estão da média e, portanto, mais homogêneos.
'''
std = np.std(array_of_scores)
print(f"Desvio padrão: {std}")
print(f"Se entrasse uma nova nota, provavelmente seria no intervalo: {mean-std} e {mean+std}")
#%%
