#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import secrets
import numpy as np


# In[4]:


def gen_password(length, use_num):
    if length <= 0:
        raise ValueError("Password Length Must Be Greater Than 0")     
    character_pool = []
    pool = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    pool_no_num = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    for i in range(length):
        if use_num:
            character_pool.append(secrets.choice(pool))
        else:
            character_pool.append(secrets.choice(pool_no_num))
    password = "".join(character_pool)
    return password



# In[7]:


gen_password(78, False)


# In[ ]:




