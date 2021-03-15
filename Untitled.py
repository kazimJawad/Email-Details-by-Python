#!/usr/bin/env python
# coding: utf-8

# In[ ]:


data = input("Enter Email Address :\n")
fpos = data.find('@')
username = data[ : fpos]
extension = data[fpos+1 :]
print('\nUser Name is :',username)
print('Extension is :',extension)

