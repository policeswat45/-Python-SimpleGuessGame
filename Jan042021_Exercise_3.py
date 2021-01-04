# With initial balance withdraw, how much saving after x months would one receives

# Type in the initial balance
a = int(input("Please choose an amount of deposits (in 1000 VND): "))
# Type in the withdraw amount
b = int(input("Please choose an amount of withdraw (in 1000 VND): "))

# Calculate the number of saving
fvmonths = (b - a)/(a*0.004)

print(f"In {fvmonths} months, your deposit will be at face value!")
