#!/usr/bin/env python
# coding: utf-8

# In[1]:


a="helaaaaabbbaaammmmmmmmmmmmmmmmmmmmmm"
cl=1
max=0
x=0
for i in range(len(a)-1):
    if (a[i]==a[i+1]):
        cl+=1
    elif (cl>max):
        max=cl
        x=i
        cl=1
    else :
        cl=1
        
if (cl>max)  :
    max=cl
    x=i
max,a[i]


# In[2]:


a=range(1,10)


# In[3]:


[x if x%2==0 else str(x)  for x in a]


# In[4]:


a=["Even" if i%2==0 else "Odd" for i in range(5)]
a


# In[5]:


a={'x':1,'y':2,'m':max,'zz':33}
sorted(a.values())


# In[6]:


[[i*j for j in range(1,11)] for i in range(7,9)]


# In[7]:


#generator function
def fib(limit): 
    a, b = 0, 1
    while a < limit: 
        yield a 
        a, b = b, a + b 
x = fib(5) 
print(x.__next__()); print(x.__next__()); 
print(x.__next__()); 
print(x.__next__()); 
print(x.__next__()); 


# In[17]:


def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)


# In[15]:


def make_multiplier_of(n):
    def multiplier(x):
        
        return x * n
    return multiplier
times3 = make_multiplier_of(3)
print(times3(4))


# In[ ]:





# In[ ]:





# In[ ]:




