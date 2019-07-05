#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[11]:


data = pd.read_csv("C:\\Users\Thanh\Desktop\hoc\pandas\Data\ChieuCaoChaVaCon.csv")


# In[12]:


data


# In[13]:


data.pivot(index="Day", columns="City")


# In[14]:


# Cái này để thay đổi từ dòng thành cột


# In[16]:


# Chúng ta cũng có thể yêu cầu chỉ hiện dòng nào


# In[17]:


data.pivot(index="Day", columns="City", values = "Precipation")


# In[25]:


data1 = pd.read_csv("C:\\Users\Thanh\Desktop\hoc\pandas\Data\ChieuCaoChaVaCon.csv")


# In[26]:


data1


# In[29]:


data1.pivot_table(index="Day", columns="City")
# cái này lấy theo trung bình


# In[32]:


data2 = data1.pivot_table(index="Day", columns="City", aggfunc="max", margins="True")
# cái này lấy theo max


# In[33]:


data2


# In[34]:


data2.to_csv("C:\\Users\Thanh\Desktop\hoc\pandas\Data\data2.csv")


# In[36]:


data1.to_csv("C:\\Users\Thanh\Desktop\hoc\pandas\Data\data3.csv", index=False, columns=["Day", "City"])
# cái này chỉ lấy day và city 
# ngoài ra còn có startrow=, startcol=
# sheetname=


# In[ ]:




