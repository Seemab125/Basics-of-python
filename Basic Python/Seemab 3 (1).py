#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Task 1: Rewrite this line so it's valid:
# if species = "cat":

if species == "cat":
  


# In[25]:


# Task 2: Code the first line of an if statement that tests whether x has the same value as y

if(x:=y):
    print("equal")


# In[28]:


# Task 3: On line 1, test whether a has the same value as b.
# On line 2, write that c equals d. 
# Don't forget to indent the second line.

if a==b:
c==d


# In[1]:


# Task 4: If total has the value of 100, then tax has the value of 2. Code both lines. Don't forget to indent
# the second line.

if total=100:
    tax=2


# In[4]:


# Task 5: If first_name is "Sherlock", then last_name is equal to "Holmes" and pal is equal to "Watson".
# Code all three lines.

first_name="sherlock"
second_name="Holmes"
pal="Watson"


# In[9]:


#   Task 6: Ask user to Enter “yes” or “no”. If user entered "yes" tell Python to print "congrats", if “no”, tell
#   python to print “better luck next time”



a='yes'
b='no'
x=str(input("Enter yes or no"))
if(x==a):
    print("congrats")
elif(x==b):
    print("“better luck next time”")





# In[10]:


#   Task 7: Code the first line of an if statement testing whether the variable total is less than 100.


if(x<100):
    
# where x is variable total


# In[11]:


#   Task 8: Write a program:
#   1. Ask user to enter a value in range of 1 -> 1000.
#   2. if the value is greater then 500, then write “greater than 500” else write “smaller than 500”.


a=float(input("Enter a value in range of 1 -> 1000. =  "))
if(a>=500):
    print("greater than 500")
else:
    print("smaller than 500")


# In[12]:


#   Task 9: Code if statement that tests whether the Difference of a and b (take input from user) is greater
#    than or equal to c= - 7.

a=float(input("Enter number 1 : "))
b=float(input("Enter number 2 : "))
c=-7
if(a-b>=c):
    print("greater than c")


# In[13]:


#  Task 10: Write an if statement that tests whether a variable is smaller than 99. If the test passes, assign 99
#   to the variable. Make up the variable name. Remember to indent the second line two spaces.

a=float(input("enter any number : "))
if(a<99):
    a=99
    


# In[16]:


#  Task 11: Write an if statement that tests whether a first variable is greater than a second variable. (Take
#  both values from the user)
#  If the test passes, make the second variable equal to the first variable. Make up the variable names.


first_variable = float(input("Enter the value of the first variable: "))
second_variable = float(input("Enter the value of the second variable: "))

if(first_variable > second_variable):
    second_variable = first_variable

print("First variable:", first_variable)
print("Second variable:", second_variable)




# In[ ]:




