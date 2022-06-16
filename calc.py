# Definte variable

welcome = "Welcome to calc.py!\nThis program will let you calcuate the surface area and volume of a sphere, a cube and a pyramid."
prompt = "\n\nPlease enter the radius/side lenght of your shape in cm:  "
pi = 3.141592

print(welcome)

response = input(prompt)

radLength = float(response)

areaSphere = 4 * pi * (radLength**2)
volSphere = (4/3) * pi * (radLength**3)
areaCube = 6 * (radLength ** 2)
volCube = radLength**3

print(f"\nThe surface area of the sphere is: {areaSphere} cm^2")
print(f"\nThe volume of the sphere is: {volSphere} cm^3")
print(f"\nThe surface area of the cube is: {areaCube} cm^2")
print(f"\nThe volume of the cube is: {volCube} cm^3")

