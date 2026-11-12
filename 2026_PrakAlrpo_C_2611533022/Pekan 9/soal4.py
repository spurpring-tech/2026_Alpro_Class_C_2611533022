# Name: Muhamad Rafi'Iy Hidayatullah
# NIM: 2611533022
# Question 4

# Example
phone = "081234567890"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked, "(contoh)")

# Output 1
phone = "081234567890"
masked = phone[:4] + "*" * (len(phone)- 7) + phone[-3:]
print(masked, "(Output 1)")

# Output 2
phone = "08123456789"
masked = phone[:4] + "*" * (len(phone)- 7) + phone[-3:]
print(masked, "(Output 2)")

# Output 3
phone = "0812345678"
masked = phone[:4] + "*" * (len(phone)- 7) + phone[-3:]
print(masked, "(Output 3)")

# Outout 4
phone = "082611533022"
masked = phone[:4] + "*" * (len(phone)- 7) + phone[-3:]
print(masked, "(Output 4)")