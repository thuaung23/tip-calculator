print("Welcome to the tip calculator.")
total = float(input("What is the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "))
num_of_people = int(input('How many people will split the bill? '))

new_total = total + (total * (percentage / 100))
payment = round(new_total / num_of_people, 2)


print(f"Each person should pay: ${payment}.")