#Write your code below this line 👇
def prime_checker(number):
    divisible_counter = 0
    for n in range(1, number):
        # print(f"{number} % {n}")
        # print(number % n)
        # print(f"divisble_counter = {divisible_counter}")
        if number % n == 0:
            divisible_counter += 1

    if divisible_counter > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
