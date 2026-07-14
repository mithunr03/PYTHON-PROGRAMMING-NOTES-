import math 
side1= float(input("Enter side A:"))
side2= float(input("Enter side B:"))

result = math.sqrt(pow(side1,2) + pow(side2,2))
print(f"Side c={round(result,2)}")