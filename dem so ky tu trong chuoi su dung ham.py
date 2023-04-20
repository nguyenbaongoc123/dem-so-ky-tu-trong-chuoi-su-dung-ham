#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_chars(txt):
    re= 0
    for i in txt:
        re+= 1
    return re
input_str = input('Your string: ')
print('Length: ', count_chars(input_str))


# In[ ]:




