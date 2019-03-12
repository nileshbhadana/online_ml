#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from numpy import pi


# In[ ]:





# In[ ]:





# In[3]:


a=np.array([1,2,4,5,7,8])


# In[ ]:





# In[4]:


b=a**3


# In[ ]:





# In[5]:


dir(plt)


# In[10]:


plt.plot(a,b,'#008000')


# In[18]:


x=np.linspace(0,2*pi,1000)


# In[ ]:





# In[13]:


x


# In[24]:


y=np.sin(x)
z=np.cos(x)


# In[ ]:





# In[ ]:





# In[22]:


y


# In[ ]:





# In[ ]:





# In[42]:


plt.plot(x,y,color="red",label='sin')
plt.plot(x,z,'-.',label='cos')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[38]:


plt.xlabel('angles')
plt.ylabel('sin(x)')
plt.grid(color='black')
plt.plot(x,y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[35]:


plt.plot(x,y,'-.',x,z,'b')


# In[ ]:





# In[ ]:





# In[ ]:





# In[31]:


plt.bar(a,b,color='red')


# In[6]:


plt.scatter(a,b,marker='^',color='green')
plt.bar(a,b)


# In[9]:


plt.barh(a,b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




