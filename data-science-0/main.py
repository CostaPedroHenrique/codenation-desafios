#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[4]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[5]:


def q2():
    # Retorne aqui o resultado da questão 2.
    df_age_gender = black_friday.loc[(black_friday['Age'] == '26-35')&(black_friday['Gender'] == 'F')]
    return len(df_age_gender)


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[6]:


def q3():
    # Retorne aqui o resultado da questão 3.
    df_unique_users = black_friday['User_ID'].unique()
    return len(df_unique_users)


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[6]:


def q5():
    # Retorne aqui o resultado da questão 5.
    df_sum_na = pd.DataFrame(black_friday.isna().sum(axis=1), columns=['sum_na'])
    return len(df_sum_na.loc[df_sum_na['sum_na'] > 0])/len(df_sum_na)
q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[9]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday.isnull().sum().max()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].mode()[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[20]:


def q8():
    # Retorne aqui o resultado da questão 8.
    normalized_df = (black_friday['Purchase'] - black_friday['Purchase'].min())/(black_friday['Purchase'].max()-black_friday['Purchase'].min())
    return normalized_df.mean()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[18]:


def q9():
    # Retorne aqui o resultado da questão 9.
    standardized_df = (black_friday['Purchase'] - black_friday['Purchase'].mean())/black_friday['Purchase'].std()
    return len(standardized_df[abs(standardized_df) <= 1])


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[15]:


def q10():
    # Retorne aqui o resultado da questão 10.
    df_na = black_friday.loc[black_friday['Product_Category_2'].isna()][['Product_Category_2', 'Product_Category_3']].isna()
    x = df_na['Product_Category_2'] == df_na['Product_Category_3']
    for _, test in enumerate(x):
        if test == False:
            validation = False
            break
        else:
            validation = True
    return validation


# In[ ]:




