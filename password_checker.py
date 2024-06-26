import string

#Printing out common password guidelines for the user to consider.
print("This program checks the strengths of the password submitted by the user.")
print("Here are some basic guidelines to ensure your password is strong:")
print("1. Password should be at least 8 characters long.")
print("2. Password should contain at least one uppercase letter.")
print("3. Password should contain at least one special character.")
print("4. Password should contain at least one digit.")
print("")
print("This program will also check if the password is found in a common list of passwords.")
print("The password list used is Xato-net-10-million-passwords-1000000.txt (can be found on github)")
print("")
password = input("Enter your password here: ")

#Checking the password for uppercase, lowercase letters, digits and special characters.
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])

#Finding the length of the password.
length = len(password)

#Initialising the score of the password to 0.
score = 0

#Adding points based on the given conditions of the password.
if length > 8:
    score += 1

if length > 12:
    score += 1

if length > 16:
    score += 1

if length > 20:
    score += 1

#Awarding points based on uppercase, lowercase letters, digits and special characters in the password.
if upper_case == 1:
    score += 1

if lower_case == 1:
    score += 1

if digits == 1:
    score += 1

if special == 1:
    score += 1

total_score = 9
count = 0
#Comparing the password with the common list of passwords from the file.
with open('xato-net-10-million-passwords-1000000.txt', 'r') as file:
    for line in file:
        if password == line.strip():
            score = 0
            print("Password is found in a common list, can be easily cracked.")
            print("You score is: ")
            print(score)
            exit()
        else:
            count += 1
            continue
    
    if count > 1:
        score += 1
#Printing the final score.
print("Final score is:")
print(str(score) + " out of 9.")

#Printing the strength of the password based on the score.
if score < 2:
    print("Password is weak. Please consider changing it.")
elif 2 < score < 5:
    print("Password is okay. Consider making it stronger.")
elif 5 < score < 7:
    print("Password is strong. Can still be stronger.")
elif 7 < score < 9:
    print("Password is very strong.")



