#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Task 1:
#   Make a calculator Which will base on your result scenario.


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


# 
