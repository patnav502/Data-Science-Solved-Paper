#!/usr/bin/env python
# coding: utf-8

# # mid-term  solved paper

# 1. create a 1D array of 9 elements using numpy module and reshape it into the 2D array of size 3*3

# In[1]:


import numpy as np


# In[3]:


x= np.arange(9)
print(x)
y= x.reshape(3,3)
print(y)


# 2.

# In[4]:


list3=[x for x in range (10) if x%2==0]
print(list3)


# 3.....

# In[6]:


x="PythonProgramming"
y=x[:6]
print(y)
z=x[6:14]
print(z)
m=x[-5:]
print(m)
t=x[:4]+x[-3:]
print(t)


# 5(a) construct a data frame using 2D list

# In[7]:


import pandas as pd


# In[9]:


data=[
    ['ram',18],
    ['shyam',17],
    ['sachin',19]
    ]
df=pd.DataFrame(data,columns=['name','age'])
print(df)


# 5(b). construct a data frame using dictionary

# In[11]:


import pandas as pd


# In[12]:


data={'name':['ram','shyam','sachin'], 'age':[18,17,19]}
df=pd.DataFrame(data)
print(df)


# 6. write a python code to discuss in detail about variance, standard deviation, covariance and correlation

# In[13]:


import numpy as np
import pandas as pd


# In[20]:


data={
     'x':[10,15,20,25,30],
     'y':[5,10,15,20,25]
}
df=pd.DataFrame(data)     
variance_x=np.var(df['x'])
variance_y=np.var(df['y'])
dev_x=np.std(df['x'])
dev_y=np.std(df['y'])
covariance=np.cov(df['x'],df['y'])[0,1]
correlation=np.corrcoef(df['x'],df['y'])[0,1]
print(variance_x)
print(variance_y)
print(dev_x)
print(dev_y)
print(covariance)
print(correlation)


# 11(a). write a python program illustrating use of box plot.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


np.random.seed(10)
D1=np.random.normal(100,10,200)
D2=np.random.normal(90,20,200)
plt.boxplot([D1,D2])
plt.xticks([1,2],['D1','D2'])
plt.ylabel('values')
plt.show()


# In[ ]:





# In[ ]:




