#!/usr/bin/env python
# coding: utf-8

# In[1]:


languages=['java', 'python','c']
versions = [14,3,6]


# In[2]:


result=zip(languages,versions)
print(list(result))


# In[3]:


data = {'Name':['Tanya','Surbhii','sia'], 'Age':[22,22,34]}


# In[6]:


import pandas as pd
dfemp1=pd.DataFrame(data)
print(dfemp1)


# In[7]:


seremplage = pd.Series(dfemp1['Age'])


# In[8]:


seremplage.head()


# In[10]:


result = seremplage.apply(lambda x : 11 if x==19 else x)
print(result)


# In[11]:


import numpy as np
array1= np.array ([1,3,5])
print("np.array():\n", array1)


# In[12]:


array2= np.zeros((3,3))
print("\nnp.zeros():\n", array2)


# In[14]:


array3= np.array([1,3,5,7,9,11])
array4= np.reshape(array3,(2,3))
array5= np.transpose(array4)
print("Original array:\n", array3)
print("Reshaped array:\n", array4)
print("Transposed array:\n", array5)


# In[15]:


array1 = np.array([[1,3,5], [2,4,6]])
np.savetxt('data.txt', array1)
loaded_data = np.loadtxt('data.txt')
print (loaded_data)


# In[ ]:




