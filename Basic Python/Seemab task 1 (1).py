#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input("Enter your name: ")
print("hello ",name)
English_marks=float(input("please enter your English_marks:"))
print(English_marks)
total_marks1=float(input("please enter your total_marks:"))
percentage=English_marks/total_marks1*100
print("your percentage in English is",percentage)


math_marks=float(input("please enter your math_marks:"))
print(math_marks)
total_marks2=float(input("please enter your total_marks:"))
print(total_marks2)
percentage=math_marks/total_marks2*100
print("your percentage in math is",percentage)


phys_marks=float(input("please enter your phys_marks:"))
print(phys_marks)
total_marks3=float(input("please enter your total_marks:"))
print(total_marks3)
percentage=phys_marks/total_marks3*100
print("your percentage in phys is",percentage)


chem_marks=float(input("please enter your chem_marks:"))
print(chem_marks)
total_marks4=float(input("please enter your total_marks:"))
print(total_marks4)
percentage=chem_marks/total_marks4*100
print("your percentage in chem is",percentage)

Grand_total_marks=total_marks1+total_marks2+total_marks3+total_marks4
print("grand total marks are", Grand_total_marks)
total_obtained_marks=English_marks+math_marks+phys_marks+chem_marks
percentagee=total_obtained_marks/Grand_total_marks *100
print("you have obtained= " , total_obtained_marks, "marks out of", Grand_total_marks)
print(name, " your total overall percentage is: ",percentagee, "%")
average=(English_marks+math_marks+phys_marks+chem_marks)/2
print(name, ", your average marks are: ", average)
print()


# In[19]:


#task1
# store your bio data (Name, roll number, age, date of birth, and gender) in the variables
name="Seemab Hassan"
roll_no= float(9)
date_of_birth="march23_2003"
gender="male"

print("name : ",name)
print("roll number :" , roll_no)
print("Date of birth : ",date_of_birth)
print("gender : ",gender)


# In[1]:


#task 2
# Write a program to convert $ into pakistani rupee.
dollars=input("Enter the amount in dollars you want to convert ")
print("entered amount is : ",float(dollars))
rupee = float(dollars)*float(286.17)
print("the amount in rupees are : ",rupee)



# In[2]:


#task 3
#take two inputs from users and then calculate these manipulations sum, subtract, multiple and division

number1=input("Enter first number : ")
number2=input("Enter second number : ")

addition=float(number1)+float(number2)
print("By Adding ",number1, "and ", number2, "we get", addition)

subtr=float(number1)-float(number2)
print("Subtracting second number from first number we get ", subtr)


# In[4]:


#task 4
#draw the following

print("*************")
print("***       ***")
print("***       ***")
print("***       ***")
print("***       ***")
print("*************")


# In[28]:


#task 5
# take 2 numbers from user and display them without floating point

num1=int(input("enter any number : "))
num2=int(input("enter second number :"))
x=(num1//num2)
print(x)


# In[2]:


#task 6 celcius to fahrenheit
#(2°C × 9/5) + 32

x=float(input("Enter temperature in celcius"))
y=float(x * 9/5 + 32)
print("temp in fahrenheit is: ", y)


# In[9]:


#Task 7: find the slope x1=5, x2=10 Where y1=3, y2=5 , b will be enter from user (m=y2-y1/x2-x1)
x1=5
x2=10
y1=3
y2=5
z=float(y2-y1/x2-x1)
print("slope is: ", z)


# In[15]:


#Task 8: Enter your height in feet and centimetres then system will display in meters

x=float(input("enter height in feet"))
y=x*30.48
print("height in centimeter is", y)
a=float(input("enter height in feet"))
b=a/3.281
print("height in meters is :",b)
f=float(input("enter height in cm"))
g=f/100
print("height in meters is:",g)


# In[23]:


#Task9: Enter your matriculation marks subject wise and the system will display total marks 
# and percentage of all also display subject wise
# percentage


a=float(input("enter math marks "))
b=float(input("enter physc marks"))
c=float(input("enter chem marks"))
d=float(input("enter urdu marks"))

total_marks=400
total_obt=a+b+c+d
x=float(total_obt/total_marks*100)
print(" you obtained ",x, "percentage")

e=a/100*100
print("math percentage: ", e)

f=b/100*100
print("phys percentage: ", f)

g=a/100*100
print("chem percentage: ", g)

h=a/100*100
print("math percentage: ", h)


# In[ ]:




