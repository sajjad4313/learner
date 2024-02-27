#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv("C:\\Users\\sajja\\Downloads\\pro1.csv")
df.head(5)


# In[3]:


df.info()


# In[4]:


df['index']=df.index +1
df.head()


# In[ ]:





# In[5]:


df.pivot_table(columns="Road_Type",values="index",aggfunc="count")


# In[6]:


df.pivot_table(columns="Speed_limit",values="index",aggfunc="count")


# In[29]:


df.pivot_table(columns=["Road_Type","Weather_Conditions"],values="index",aggfunc="count")


# In[8]:


df.pivot_table(columns="Urban_or_Rural_Area",values="index",aggfunc="count")


# In[9]:


df.pivot_table(columns="Light_Conditions",values="index",aggfunc="count")


# # d
# 

# In[10]:


df.pivot_table(columns=["Speed_limit","Road_Type"],values="index",aggfunc="count")


# In[11]:


df.pivot_table(columns=["Road_Surface_Conditions","Road_Type"],values="index",aggfunc="count")


# In[12]:


x=df.index
y=df.Road_Type
plt.title("Road type")
plt.ylabel("No of Accidents")

plt.hist(y)
plt.show()


# In[ ]:





# In[13]:


sns.countplot(x="Road_Type",data=df)


# In[14]:


sns.countplot(x="Road_Surface_Conditions",data=df)


# In[15]:


sns.countplot(x="Speed_limit",data=df)


# In[16]:


sns.countplot(x="Urban_or_Rural_Area",data=df )


# In[25]:


plt.figure(figsize=(15,5))
plt.subplot(2,2,1)
sns.countplot(x="Speed_limit",data=df)
plt.subplot(2,2,2)
sns.countplot(x="Road_Surface_Conditions",data=df)
plt.subplot(2,2,3)

sns.countplot(x="Road_Type",data=df)
plt.show()


# In[27]:


plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
sns.countplot(x="Road_Type",data=df)
plt.subplot(1,2,2)
sns.countplot(x="Road_Surface_Conditions",data=df)


# In[ ]:





# In[ ]:




