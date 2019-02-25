def gcd(x, y):
    while y:
        z = x
        x = y
        y = z % y

    return x

print(gcd(15, 20))
