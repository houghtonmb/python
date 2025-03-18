# variables for the revenue of each item
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

# Variable to calculate total revenue
income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

# Initial outputs
print("Earned amount:")
print("Bubblegum: $",bubblegum)
print("Toffee: $",toffee)
print("Ice cream: $",ice_cream)
print("Milk Chocolate: $",milk_chocolate)
print("Doughnut: $",doughnut)
print("Pancake: $",pancake)

# Final calculation output
print("Income: $",income)
staff_expenses = int(input("Staff expenses: "))
other_expenses = int(input("Other expenses: "))
net_income = income - (staff_expenses + other_expenses)
print("Net Income: $", net_income)
