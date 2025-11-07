def gcd(a, b):
    # Algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a

# Teste com os valores dados
a = 26513
b = 32321
print("Exercice:1")
print(f"The gcd() of {a} and {b} is {gcd(a, b)}")


def extended_gcd(a, b):
    if b == 0:
        return (1, 0, a)
    else:
        x, y, g = extended_gcd(b, a % b)
        return (y, x - (a // b) * y, g)

p = 26513
q = 32321
u, v, g = extended_gcd(p, q)
print("::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("Exercice:2")
print(u, v, g)   # prints: 10245 -8404 1
print(p*u + q*v) # prints: 1




print("::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("Exercice:3")
# Primeiro cálculo: 11 mod 6
x = 11 % 6
print("x =", x)

# Segundo cálculo: 8146798528947 mod 17
y = 8146798528947 % 17
print("y =", y)

# Menor dos dois
smaller = min(x, y)
print("The smaller number:", smaller)


