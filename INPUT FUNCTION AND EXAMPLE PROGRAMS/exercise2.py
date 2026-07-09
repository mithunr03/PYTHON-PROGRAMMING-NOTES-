# Shopping Calculator
item=input("What item do you want to buy?:")
price=float(input(f"What is the price of {item}?:"))
quantity=int(input(f"How many {item} do you want to buy?:"))
total= price*quantity
print(f"The total cost of {quantity} {item} is ${total}")