import math

# Input coefficients
a, b, c = map(int, input("").split())

# Calculate the discriminant
D = b**2 - 4*a*c

# Check the nature of the roots
if D > 0:
    # Real and different roots
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(f"root1 = {root1:.2f}")
    print(f"root2 = {root2:.2f}")
elif D == 0:
    # Real and same roots
    root = -b / (2*a)
    print(f"root1 = root2 = {root:.2f}")
else:
    # Imaginary roots
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    print(f"root1 = {real_part:.2f}+{imag_part:.2f}i")
    print(f"root2 = {real_part:.2f}-{imag_part:.2f}i")
