#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? 
eg:- values can be integer or string and expressions will be mathematical operators.
        *,'hello',-87.8,-,/,+,6.

Answer =       
values= -87.8, 6, 'hello'
Mathematical operator= *, - , / , +.


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

Answer = Strings are sequences of characters. A String is usually words, enclosed with "" ,''
         variable is used for data storage or assigning value


# In[ ]:


3. Describe three different data types.

Answer = 1) Numeric data type
         integer: Real Numbers without decimal. Eg. 56
         float:  Eg. 3.14
        complex: 5i+2j
        
        2) boolean data type 
          bool(True,False)
        
        
        3)Text data type:
            string:  Eg. "name"


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

Answer = Expression is made up of values and mathematical operators.
         b=6+2


# In[ ]:


5. This assignment statements, like spam = 10. What is the difference between an
get_ipython().set_next_input('expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

Answer = Expression is made up of values, containers, and mathematical operators (operands) and the 
statement is just like a command that a python interpreter executes like print.


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1

Answer = 23


# In[2]:


bacon = 22
bacon + 1


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' +'spamspam'
'spam' * 3

Answer = 'spamspamspam'
         'spamspamspam'


# In[10]:


'spam' +'spamspam'


# In[9]:


'spam' * 3


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Answer = because eggs is all alphabate and 100 is number
  


# In[ ]:


9. What three functions can be used to get the integer, floating-point number, or string
get_ipython().set_next_input('version of a value');get_ipython().run_line_magic('pinfo', 'value')

Answer =int()
        float()  
        str()
        


# In[ ]:


get_ipython().set_next_input('10. Why does this expression cause an error? How can you fix it');get_ipython().run_line_magic('pinfo', 'it')
I have eaten + 99 + burritos.

Answer = Expression will cause error because it consists of two different data types.
To fix it, we have to convert int to string.
print("I have eaten " + "99 " + "burritos ")


# In[3]:


print("I have eaten " + "99 " + "burritos ")


# In[ ]:




