a = int(input("Write a: "))
b = int(input("Write b: "))
c = int(input("Write c: "))

result1 = (-b + (b - 4 * a * c)**0.5)/(2*a)
result2 = (-b - (b - 4 * a * c)**0.5)/(2*a)

print("First Result: ", result1)
print("Second Result: ", result2)