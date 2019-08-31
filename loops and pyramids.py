#!/usr/bin/env python
# coding: utf-8

# # Loops

# By default inside the print statement, end='\n':- which prints each print statement in new line
# Instead of new line we just put end = ' ' so that each print statement after printing/outputting,
# prints to the same line which are separeted by whatever is value of end inside print statement.

# ## NO. 1

# In[2]:


for i in range(1,10): # This loop is responsible to run the for loop and hit enter using the last print statement
    for j in range(i): # This loop is responsible to print as much 'X' as the loop runs(IN A LINE)
        print('X', end = ' ')
    print('') #This is for enter/ To enter to the next line


# ## NO. 2

# To get the mirror image of above half-pyramid,
# We have to understand and know what we are going to built.
# We have to know the output before hitting the code.
# In the below, 
# (1). The number of spaces are decreasing and the 
#     number of 'X' are increasing.
# (2) We have to print the spaces then 'X'.

# In[4]:


for i in range(1,10):
    for j in range(9-i):
        print(' ', end=' ')
    for k in range(i):
        print('X', end= ' ')
    print()


# ## NO.3

# After understanding what we have to print, we have practice as below

# In[5]:


for i in range(1,10):
    for j in range(9-i):
        print('X', end=' ')
    print()


# ## NO. 4

# In[7]:


for i in range(1, 10):
    for j in range(i):
        print(' ', end=' ')
    for k in range(9-i):
        print('X', end=' ')
    print()


# ## NO. 5

# I have just combined the NO-2 first then NO-1. (But still the pyramid is not looking great)

# In[11]:


for i in range(1, 10):
    for j in range(9-i):
        print(' ', end=' ')
    for k in range(i):
        print('X', end= ' ')
    for m in range(i):
        print('X', end= ' ')
    print()


# ## NO. 6

# I have combined NO. 2 then NO.1 and to make a perfect pyramid I have reduce a loop of end 'X'.
# In the below the last for loop at the begining has a value of 0, so doesnot runs at the first time so
# the output looks like pyramid.

# In[12]:


.for i in range(1, 10):
    for j in range(9-i):
        print(' ', end=' ')
    for k in range(i):
        print('X', end= ' ')
    for m in range(i-1): # Loop is responsible to make a perfect pyramid, just compare NO.5 and NO. 6
        print('X', end= ' ') 
    print()


# ## NO. 7

# ###### Same as NO.5, We have only altered the spaces and X

# In[14]:


for i in range(1, 10):
    for j in range(i):
        print(' ', end=' ')
    for k in range(9-i):
        print('X', end=' ')
    for m in range(9-i):
        print('X', end=' ')
    print()


# ## NO. 8

# Compare this with No. 6/ YOu will get the idea

# In[16]:


for i in range(1, 10):
    for j in range(i):
        print(' ', end=' ')
    for k in range(9-i):
        print('X', end=' ')
    for m in range((9-i)-1): # subtracting 1 inside the loop, so that the loop run one less time
        print('X', end=' ')
    print()


# In[ ]:




