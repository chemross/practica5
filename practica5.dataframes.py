#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


#ejercicio 2


# In[7]:


import pandas as pd 
  
list = ['10', '20', '10'] 
   
ser = pd.Series(list) 
print(ser)


# In[8]:


import pandas as pd 
  
list = ['rojo', 'verde', 'azul'] 
   
ser = pd.Series(list) 
print(ser)


# In[5]:


#ejercio3


# In[25]:


import pandas as pd
df = pd.DataFrame()


# In[26]:





df['series'] =['10','20','10']


print(df)


# In[27]:





df['series'] = ['rojo', 'verde', 'azul']


print(df)


# In[ ]:


#ejercio 4


# In[10]:


import pandas as pd


# In[11]:


pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/avengers.csv')


# In[19]:


import pandas as pd


# In[20]:


df = pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/avengers.csv', delimiter=',') 

print(df)



# In[ ]:


#5


# In[21]:


df3 = pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/avengers.csv')
print(df3.head())


# In[22]:


df3 = pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/avengers.csv')
print(df3.head(10))


# In[ ]:





# In[24]:


df.iloc[-5:]


# In[ ]:





# In[ ]:


#6


# In[26]:


df.size


# In[ ]:


#7


# In[48]:


df.dtypes


# In[29]:


#8


# In[49]:


df.index


# In[50]:


df.fecha_inicio


# In[ ]:


#9


# In[51]:


df.reset_index()


# In[ ]:





# In[ ]:





# In[ ]:




