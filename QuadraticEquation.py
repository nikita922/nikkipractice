# To solve a quadratic equation
import cmath
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
disc = (b**2)-4*a*c
x1 = (-b+cmath.sqrt(disc))/2*a
x2 = (-b-cmath.sqrt(disc))/2*a
print("The solutions are {} and {}".format(x1,x2))