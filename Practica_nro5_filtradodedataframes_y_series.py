#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/airbnb.csv')


# In[3]:


df.sample(10)


# In[4]:


df.describe()


# In[5]:


df.plot.scatter(y="room_id",x="overall_satisfaction")


# In[12]:


serie= df.room_type.value_counts()
serie.plot.pie(autopct='%1.1f%%')


# In[16]:


serie=df.overall_satisfaction.value_counts()
serie.plot.pie(autopct='%1.1f%%')


# In[ ]:


#CASO 2


# In[ ]:





# In[ ]:





# In[39]:


import pandas as pd
 

df = pd.DataFrame({'nombre': ['Roberto', 'Carla'],'id': [97503, 90387]})
 

escrito = pd.ExcelWriter('roberto.xlsx')

df.to_excel(escrito,'Airbnb')

escrito.save()
print('El DataFrame se ha escrito con éxito en el archivo de Excel.')


# In[ ]:


#caso3


# In[43]:




import pandas as pd
import matplotlib.pyplot as plt


# In[44]:


df=pd.read_csv('Python5/Modulo5/Ejercicios/src/pandas/airbnb.csv')


# In[45]:


df.sample(10)


# In[46]:


df.describe()


# In[47]:


df.plot.scatter(y="room_id",x="price")


# In[ ]:




