# the input function takes every input from the user as a string. If we want to take input as an integer or float,
# we need to convert it into int or float using int() or float() function.

age1=input("Enter your age :")
age = int(age1)
age = age + 5
print(f"Your age after 5 years will be {age}")


# OR we can also write the above code in a single line as shown below.


age = int(input("Enter your age: "))
age = age + 5
print(f"Your age after 5 years will be {age}")