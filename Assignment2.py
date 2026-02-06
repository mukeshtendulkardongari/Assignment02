# 1. Datatype Identification

# Write a Python program that takes five different values as input (integer, float, string, boolean, and list) and prints the datatype of each value.

integer_val=int(input("Enter a integer value:"))
float_val=float(input("Enter Float value:"))
string_val=str(input("Enter String value:"))
lst=input("Enter list elements seperated by comma:")
lst=lst.split(",")
bool_val=input("Enter a Boolean value:")
bool_val=bool(bool_val)

print("Data type of integer value is:",type(integer_val))

print("Data type of float value is:",type(float_val))

print("Data type of string value is:",type(string_val))

print("Data type of list value is:",type(lst))

print("Data type of boolean value is:",type(bool_val))


# 2. Variable Swapping

# Write a Python program to swap the values of two variables:
# Display the values before and after swapping.
# without using a third variable

a=5
b=89

print(f"Before swapping a:{a} , b:{b}")
a,b=b,a
print(f"After swapping a:{a} , b:{b}")

# using a third variable

a=20
b=30

print(f"Before swapping a:{a} , b:{b}")

temp=a
a=b
b=temp
print(f"After swapping a:{a} , b:{b}")


# 3. Type Conversion Challenge

# Write a Python program that takes an integer and a float as input converts the integer to float converts the float to integer prints the converted values and their datatypes

int_val=int(input("Enter integer value:"))
float_val=float(input("Enter float value:"))

int_val=float(int_val)
float_val=int(float_val)

print(f"Converted integer value to float value is:{int_val} and datatype is {type(int_val)}")

print(f"Converted float value to integer value is:{float_val} and datatype is {type(float_val)}")

# 4. Arithmetic Operations with Variables

# Write a Python program that stores two numbers in variables performs addition, subtraction, multiplication, division, and modulus prints the result of each operation along with its datatype

a=23
b=12

print(f"Addition of a and b is:{a+b} Datatype is{type(a+b)}")
print(f"Subtraction of a and b is:{a-b} Datatype is {type(a-b)}")
print(f"Multiplication of a and b is:{a*b} Datatype is {type(a*b)}")
print(f"division of a and b is:{a/b} Datatype is {type(a/b)}")
print(f"Modulos of a and b is:{a%b} Datatype is {type(a%b)}")


# 5. String and Numeric Variable Combination

# Write a Python program that stores a name in a string variable stores an age in an integer variable prints a sentence combining both variables (example: "My name is Alex and I am 20 years old")

name="Mukesh Tendulkar Dongari"
age=21

print(f"My name is {name} and I am {age} years old")