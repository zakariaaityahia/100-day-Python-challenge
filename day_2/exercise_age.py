age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
last_age = 90
# my solution
current_age_int = int(age)
last_age_int = int(last_age)
#current_age_weeks = current_age_int * 52
#last_age_weeks = last_age_int * 52
#weeks_left = last_age_weeks - current_age_weeks
weeks_left = ((last_age_int - current_age_int) * 52)
print(f"You have {weeks_left} weeks left.")

