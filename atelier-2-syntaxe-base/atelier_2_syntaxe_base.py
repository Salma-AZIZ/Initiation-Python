
# Atelier 2 - Syntaxe de base en Python

# 1. Opérations arithmétiques
a = 10
b = 5

# Calculs
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
puissance = a ** b

print("Addition:", addition)
print("Soustraction:", soustraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Puissance:", puissance)

# 2. Condition
if a > b:
    print(f"{a} est supérieur à {b}")
else:
    print(f"{a} n'est pas supérieur à {b}")

# 3. Boucle for
print("Boucle for de 1 à 10:")
for i in range(1, 11):
    print(i)

# 4. Boucle while
print("Boucle while décrémentant b:")
while b > 0:
    print("b =", b)
    b -= 1
