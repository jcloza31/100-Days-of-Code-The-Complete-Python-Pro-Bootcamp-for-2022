age = input("What is your current age? ")
average_age = 90
current_age = int(age)
remaining_age = average_age - current_age
days = 365 * remaining_age
weeks = 52 * remaining_age
months =  12 * remaining_age

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)
