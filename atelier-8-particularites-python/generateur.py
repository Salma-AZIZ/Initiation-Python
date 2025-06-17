def generateur_nombres_pairs(n):
    for i in range(n):
        yield i * 2

# Utilisation
print("Premiers 10 nombres pairs générés :")
for nombre in generateur_nombres_pairs(10):
    print(nombre)
