# Name: Muhamad Rafi'Iy Hidayatullah
# NIM: 2611533022
# Question 6

# Username Kampus 1
full_name = "  Siti Aisyah  "
nim = "2610511023"
full_name = full_name.strip().lower()
stop = full_name.find(" ")
print(full_name[0:stop] + nim[-3:])

# Username Kampus 2
full_name = "Muhamad Rafi Pratama"
nim = "2610511045"
full_name = full_name.strip().lower()
stop = full_name.find(" ")
print(full_name[0:stop] + nim[-3:])

# Username Kampus 3
full_name = "Kartika"
nim = "2610511007"
full_name = full_name.strip().lower()
stop = full_name.find(" ")
print(full_name[0:stop] + nim[-3:])

# Username Kampus 4
full_name = "Muhamad Rafi'Iy Hidayatullah"
nim = "2611533022"
full_name = full_name.strip().lower()
stop = full_name.find(" ")
print(full_name[0:stop] + nim[-3:])
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().