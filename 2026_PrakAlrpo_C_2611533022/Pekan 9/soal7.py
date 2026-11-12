# Name: Muhamad Rafi'Iy Hidayatullah
# NIM: 2611533022
# Question 7

name = "muhamad rafi'iy hidayatullah"
stop = name.find(" ")
nim = "2611533022"
tahun_daftar = 2026
print("="*50)
print("STUDENT CARD".center(50))
print("="*50)
print("Name".ljust(10),":",name.title())
print("NIM".ljust(10),":",nim)
print("Username".ljust(10),":",name[0:stop]+nim[-3:])
print("Intake".ljust(10),":",tahun_daftar)
print("="*50)