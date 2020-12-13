#!/usr/bin/env python
# coding: utf-8

# Assignment No.4

# Q.1.Write down a program in Python for Opening a File and Writing " I Love LetsUpgrade" And close
# it, and read it back again, and then append some data to it and close it.

# In[9]:


#Create A File

xyz=open("Hi.txt",'w')
xyz.write("I Love LetsUpgrade")
xyz.close()


# In[10]:


xyz=open("Hi.txt",'r')
xyz.read()


# In[13]:


xyz=open("Hi.txt",'a')
xyz.write("I am a Teacher")
xyz.close()


# Q.2.Write a function which can return a Factorial of any numbers as INT, given in the argument.

# In[48]:


n=3
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
 
print("The factorial of ",n," is: ",fact(n))


# In[ ]:





# In[ ]:





# In[ ]:




