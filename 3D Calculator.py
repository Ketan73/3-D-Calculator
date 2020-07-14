import math

print("""
This is a simple 3D structure calculator.
Use it and enjoy!!
""")
Shape = input('Shape: ')

if Shape.upper() == "CUBE":
    a = input('What is the side? ')
    a = float(a)
    print("Volume: ", a ** 3)
    print("Total Surface Area: ", 6 * a ** 2)
    print("Lateral Surface Area: ", 4 * a ** 2)
elif Shape.upper() == "CUBOID":
    l = input('What is the length? ')
    b = input('What is the breadth? ')
    h = input('What is the height? ')
    l = float(l)
    b = float(b)
    h = float(h)
    print("Volume: ", l * b * h)
    print("Total Surface Area: ", 2 * (l * b + b * h + l * h))
    print("Lateral Surface Area: ", 2 * (l + b) * h)
elif Shape.upper() == "CONE":
    r = input('Whats is the radius of cone? ')
    h = input("What is it's height? ")
    r = float(r)
    h = float(h)
    s = math.sqrt(h ** 2 + r ** 2)
    s = float(s)
    print("Volume: ", math.pi * r ** 2 * h / 3)
    print("Total Surface Area: ", (math.pi * r * s) + (math.pi * r ** 2))
    print("Lateral Surface Area: ", math.pi * r * s)
elif Shape.upper() == "CYLINDER":
    r = input('Whats is the radius of cylinder? ')
    h = input("What is it's height? ")
    r = float(r)
    h = float(h)
    print("Volume: ", math.pi * r ** 2 * h)
    print("Total Surface Area: ", (2 * math.pi * r * h) + 2 * (math.pi * r ** 2))
    print("Lateral Surface Area: ", math.pi * r * h)
elif Shape.upper() == "SPHERE":
    r = input('Whats is the radius of sphere? ')
    r = float(r)
    print("Volume: ", 4 * math.pi * r**3 / 3)
    print("Surface Area: ", 4 * math.pi * r**2)
elif Shape.upper() == "HEMISPHERE":
    r = input(f"What is the radius of hemisphere? ")
    r = float(r)
    print("Volume: ", 2 * math.pi * r**3 / 3)
    print("Total Surface Area: ", 3 * math.pi * r**2)
    print("Lateral Surface Area: ", 2 * math.pi * r**2)
else:
    print("Sorry I don't understand!!")