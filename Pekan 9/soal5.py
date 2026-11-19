# Name: Muhamad Rafi'Iy Hidayatullah
# NIM: 2611533022
# Question 5

# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

# Bagian A: Username
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif username.isalnum() == False:
    print("Invalid: letters and digits only")
elif username[0].isalpha() == False:
    print("Invalid: must start with a letter")
else:
    print("Valid")

# Bagian B: NIM
nim = input("NIM: ")
if len(nim) != 10:
    print("Invalid NIM")
elif nim.isdigit() == False:
    print("Invalid NIM")
else:
    print("Valid,","intake year 20"+nim[-2:])