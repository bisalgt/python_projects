#!/usr/bin/env python
# coding: utf-8

# # Naming all files at once using os.walk('') and  os.rename('old', 'new')

# In[1]:


import os


# #### This below code helps to rename all the files at once

# In[4]:


os.listdir()


# In[7]:


os.getcwd()


# In[8]:


os.chdir('d:\\New folder')


# In[10]:


i = 1
for dir_path, dir_names, file_names in os.walk('d:\\New folder'):
    for file in file_names:
        os.rename(file, f'renamed_file_{i}')
        i += 1


# In[9]:


os.getcwd()


# In[ ]:




