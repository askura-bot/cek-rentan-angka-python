#+++++3-----10+++++
angka_tebakan = int(input("masukkan angka kurang dari 3 atau kurang dari 10: "))

isKurangDari3 = (angka_tebakan < 3)
isLebihDari10 = (angka_tebakan > 10)

print (isKurangDari3)
print (isLebihDari10)

isCorrect = isKurangDari3 or isLebihDari10
print (f"angka yang anda masukkan: {isCorrect}")

#-----3+++++10-----
angka_tebakan = int(input("masukkan angka lebih dari 3 dan kurang dari 10: "))

isLebihDari3 = (angka_tebakan > 3)
isKurangDari10 = (angka_tebakan < 10)

print (isLebihDari3)
print (isKurangDari10)

isCorrect = isLebihDari3 and isKurangDari10
print (f"angka yang anda masukkan: {isCorrect}")

#-----0+++++5-----10+++++15-----
angka_tebakan = int(input("masukkan angka > 0 < 5 atau > 10 < 15: "))

# isLebihDari0 = (angka_tebakan > 0)
# isKurangDari5 = (angka_tebakan < 5)
# isLebihDari10 = (angka_tebakan > 10)
# isKurangDari15 = (angka_tebakan < 15)

# isCorrect = ((isLebihDari0 and isKurangDari5) or (isLebihDari10 and isKurangDari15))
isCorrect = (0 < angka_tebakan < 5 or 10 < angka_tebakan < 15)

print (f"angka yang anda masukkan: {isCorrect}")

#+++++0-----5+++++10-----15+++++
angka_tebakan = int(input("masukkan angka < 0 atau > 5 < 10 atau > 15: "))

# isKurangDari0 = (angka_tebakan < 0)
# isLebihDari5 = (angka_tebakan > 5)
# isKurangDari10 = (angka_tebakan < 10)
# isLebihDari15 = (angka_tebakan > 15)

# isCorrect = ((isKurangDari0 or isLebihDari5) and (isKurangDari10 or isLebihDari15))
isCorrect = (0 >angka_tebakan or 5 < angka_tebakan < 10 or angka_tebakan > 15)

print (f"angka yang anda masukkan: {isCorrect}")