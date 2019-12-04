#!/usr/bin/env python
# coding: utf-8

# # 1. Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# 

# In[1]:


g = raw_input("Enter a string : ")
print(" \n OUTPUT: \n")
g =g.replace('little star,', 'little star,\n\t')
g= g.replace('How I wonder what you are!', 'How I wonder what you are!\n\t\t')
g=g.replace('Up above the world so high,', 'Up above the world so high, \n\t\t')
g= g.replace ('Like a diamond in the sky.','Like a diamond in the sky.\n')

print(g)


# # 2. Write a Python program to get the Python version you are using

# In[10]:


import sys
print("Current Python version")
print (sys.version)


# # 3. Write a Python program to display the current date and time

# In[11]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.today().strftime("%Y-%m-%d %H:%M:%S"))


# # -4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504
# 
# 

# In[14]:


from math import pi
r = input ("Radius of the circle : ")
Area= pi * r**2
print ("Area=" + str(Area))


# # 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

# In[19]:


fname=raw_input("Your First name?")
lname=raw_input("Your Last name?")
print( fname + " "+ lname)


# # 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output : 
# List : ['3', ' 5', ' 7', ' 23'] 
# Tuple : ('3', ' 5', ' 7', ' 23')
# 
# 

# In[1]:


values = input("Input CSV: ")
print("Tuple:")
print (tuple(values.split(',')))

print("List:")
print (list(values.split(',')))


# # 7. Write a Python to find local IP addresses using Python's stdlib

# In[4]:


import socket    
hostname = socket.gethostname()    
IP = socket.gethostbyname(hostname)    
print("Your IP Address:" + IP)


# # 8. Write a Python program to empty a variable without destroying it.
# 
# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}
# 
# 

# In[5]:


data = {"x":200}
print(type(data)())
#or
data=20
data = data.clear()
print(data)


# # 9.Write a Python program to find the location of Python module sources.
# posix 
# Platform name: 
# Linux 
# Platform release:
# 4.4.0-47-generic 
# 
# 

# In[7]:


import os, platform
print(os.name)
print("Platform name:")
print(platform.system())
print("Platform release:")
print(platform.release())


# # 10. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# Sample numbers list :
# 
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# 
# 

# In[9]:


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 
           978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 
           67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 
           831, 445, 742, 717, 958,743, 527 ]
# Nothing after 237 in the sequence 
for x in numbers:
    if x==237:
        print("...Stopping at 237...")
        break;
    elif x % 2 == 0:
        print(x)


# In[12]:


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 
           978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 
           412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 
           67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 
           831, 445, 742, 717, 958,743, 527 ]
# nothing greater than 237
for x in numbers:
    if x<237:
        if x % 2 == 0:
            print(x)


# In[ ]:




