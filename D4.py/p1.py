'''
------ OPERATORS -----

Operators are the spcial symbols that are uesed to perform specific task between two operands/variables.

eg; +, -, *, /, %

in the operation a+b ; a and b are oprands / variables and + is the operator which is used to perform addition operation between a and b.
+ ---> used for addition
 
----- TYPES OF OPERATORS -----
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Membership Operators
6. Identity Operators

'''

# ARITHEMETIC OPERATORS

first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number: "))

print(f"Addition of {first_number} and {second_number} is : {first_number + second_number}")
print(f"Subtraction of {first_number} and {second_number} is : {first_number - second_number}")
print(f"Multiplication of {first_number} and {second_number} is : {first_number * second_number}")
print(f"Division of {first_number} and {second_number} is : {first_number / second_number}")
print(f"Modulus of {first_number} and {second_number} is : {first_number % second_number}")
print(f"power of {first_number} and {second_number} is : {first_number ** second_number}")

#Difference between / and // is that / gives the float value and // gives the integer value.

 print(f"Floor Division of {first_number} and {second_number} is : {first_number // second_number}")

# area of circle

raduis=float(input("enter the radius of the circle"))
area_of_circle=3.14*raduis*raduis 

# we can also write the above formula as
# area_of_circle=3.14*radius**2

print(f"Area of circle is : {area_of_circle}")

#simple interest

p=int(input("enter the principle amount"))
t=float(input("enter the time in years"))
r=float(input("enter the rate of interest"))

simple_interest=(p*t*r)/100
print(f"simple interest is :{simple_interest}")