print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

no_of_t = lower_case_name1.count('t') + lower_case_name2.count('t')
no_of_r = lower_case_name1.count('r') + lower_case_name2.count('r')
no_of_u = lower_case_name1.count('u') + lower_case_name2.count('u')
no_of_e = lower_case_name1.count('e') + lower_case_name2.count('e')
no_of_l = lower_case_name1.count('l') + lower_case_name2.count('l')
no_of_o = lower_case_name1.count('o') + lower_case_name2.count('o')
no_of_v = lower_case_name1.count('v') + lower_case_name2.count('v')


total_true_letters = no_of_t + no_of_r + no_of_u + no_of_e
total_love_letters = no_of_l + no_of_o + no_of_v + no_of_e
str_total_score = str(total_true_letters) + str(total_love_letters)
int_total_score = int(str_total_score)

if int_total_score < 10 or int_total_score > 90:
    print(f"Your score is {int_total_score}, you go together like coke and mentos."
)
elif int_total_score > 40 and int_total_score < 50:
    print(f"Your score is {int_total_score}, you are alright together."
)
else:
    print(f"Your score is {int_total_score}.")

