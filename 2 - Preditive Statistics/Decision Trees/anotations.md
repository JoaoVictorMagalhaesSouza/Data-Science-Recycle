# Estudando sobre Árvores de Decisão

## Definições
- Consiste, basicamente, em uma série de regras de divisão.
- Os nós internos consistem nas regras, enquanto os nós folha consistem nos valores das médias das observações que atendem às regras da sua ramificação.
- O grande objetivo é dividir os dados em regiões ou espaços/regiões que representem as regras de divisão.

## Como acontece o processo de criação dos espaços/regiões?
1) Dividir as variáveis preditoras em J espaços/regiões que não se sobrepõem, isso é, dado uma observação x1 de da variável preditora X1, que está contida na região R1, não deve existir outra Rj que contenha x1 de X1.
2) Para cada observação em uma região Rj, a predição será a média de Y da Rj para qualquer x contido nessa Rj.
3) Exemplo: dado que temos 2 regiões, R1 e R2, cujo a média de Y é 10 e 20, respectivamente: para qualquer X = x contido em R1, o Y predito será 10 e, para qualquer X = x contido em R2, o Y predito será 20.

## Mas como dividir os J espaços ou regiões?
- Encontrar caixas R1, R2, ..., Rj que minimizam o RSS:
    - $$ \sum_{j=1}^{J} \sum_{i\in{R_{j}}} (y_{i} - \hat{y}_{R_{j}})^{2} $$