#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 


# In[11]:


import pandas as pd 


# In[8]:


import seaborn as sns


# In[9]:


import matplotlib.pyplot as plt 


# In[10]:


df=pd.read_csv("cpi_2007_2018-CSV.csv") 
df 


# In[22]:


df.head() 


# In[23]:


df.tail()


# In[24]:


df.shape


# In[25]:


df.info


# In[30]:


#percentage of missing values 
df.isnull().sum() 


# In[29]:


df.isnull().sum() /df.shape[0]*100


# In[31]:


#finding duplicated values 
df.duplicated().sum() 


# In[42]:


df.describe().T


# In[46]:


for i in df.select_dtypes(include="number").columns:
    sns.histplot(data=df, x=i) 
    plt.show() 


# In[44]:


for i in df.select_dtypes(include="number").columns:
    sns.boxplot(data=df, x=i) 
    plt.show() 


# #scattering plot to understand the r/ships of each dataset/ target data vs dependant data

# In[12]:


df.select_dtypes(include="number").columns


# In[52]:


for i in ['yr', 'month', 'allitems', 'food_non_alcoholic', 
       'clothing', 'utilities', 'furnishing', 'health', 'transport',
       'communication', 'recreation', 'education', 'restaurant',
       'miscellaneous', 'CPI excluding unprocessed food and petrol', 'food',
       'bread &cereals', 'Meat', 'fish', 'dairy', 'oils_fats', 'fruits',
       'vegetables', 'sugar', 'Food products n.e.c.', 'offexch', 'paraexch',
       'goprice_usd', 'pprice']:
    sns.scatterplot(data=df, x=i,y='beverages') 
    plt.show() 


# In[1]:


#correlation with heatmap to interpret the relation & multicolliniarityabs


# In[13]:


df.select_dtypes(include="number").corr() 


# In[17]:


s=df.select_dtypes(include="number").corr() 
plt.figure(figsize=(15,15)) 
sns.heatmap(s,annot=True) 


# In[ ]:





# In[ ]:




