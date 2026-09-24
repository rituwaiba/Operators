'''
----- LOGICAL OPERATION -----

types of logical operators:

1. AND

----- AND operator -----
C1 C2 Result
T T T
T F F
F T F
F F F

2. OR

----- OR operator -----
C1 C2 Result
T T T
T F T   
F T T
F F F

3. NOT

----- NOT operator -----
C Result
T F
F T

'''

a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("Enter the third number"))

print(a>b and a>c)
print(a<b and a<c)

print(a>b or a>c)
print(a<b or a<c)