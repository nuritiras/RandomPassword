import random

karakrer = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

uzunluk = int(input("Şifre kaç karakterden oluşturulsun : "))
password = ""
for x in range(0, uzunluk):
    password_char = random.choice(karakrer)
    password = password + password_char
print("Random Şifreniz : ", password)