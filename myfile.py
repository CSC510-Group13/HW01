import math

def solve_quadratic(a, b, c):
    if a == 0:
        return "Not a quadratic equation."
    
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Roots are: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One root: {root}"
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-discriminant) / (2 * a)
        return f"Roots are: {real} + {imag}i and {real} - {imag}i"

a = float(input("a: "))
b = float(input("b: ")) # i removed a ) to throw error in the demo
c = float(input("c: "))

print(solve_quadratic(a, b, c))
