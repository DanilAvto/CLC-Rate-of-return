#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt


# In[2]:


PG = wb.DataReader('PG', data_source = 'yahoo', start ='1995-1-1')


# In[3]:


PG.head()


# In[4]:


PG.tail()


# In[6]:


PG['Simple Return'] = (PG['Adj Close']/PG['Adj Close'].shift(1)) - 1
print (PG['Simple Return'])


# In[7]:


PG['Simple Return'].plot(figsize = (8,5))


# In[12]:


avg_returns_d = PG['Simple Return'].mean()
avg_returns_d


# In[13]:


avg_returns_a = PG['Simple Return'].mean()* 250
avg_returns_a


# In[18]:


print (str(round(avg_returns_a, 5) * 100) + '%')


# In[19]:


PG.head()


# In[21]:


PG['log return'] = np.log(PG['Adj Close']/PG['Adj Close'].shift(1))
print(PG['log return'])


# In[23]:


PG['log return'].plot(figsize =(8,5))


# In[24]:


Log_return_d = PG['log return'].mean()


# In[25]:


Log_return_d


# In[28]:


Log_return_a = PG['log return'].mean() * 250


# In[29]:


Log_return_a


# In[50]:


print (str(round(Log_return_a,2) *100) + '%')


# In[ ]:




