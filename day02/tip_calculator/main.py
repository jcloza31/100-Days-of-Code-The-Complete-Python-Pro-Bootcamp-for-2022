welcome_message = "Welcome to the tip calculator."
print(welcome_message)

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to  give? 10, 12, or 15? "))
no_of_pax = int(input("How many people to split the bill? "))

tip_percentage = (tip / 100) 
total_bill = bill * (1 + tip_percentage)
bill_per_pax = "{:.2f}".format(total_bill / no_of_pax)

result = f"Each person should pay: ${bill_per_pax}"
print(result)
