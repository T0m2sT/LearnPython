a = int(input("Write a: "))
b = int(input("Write b: "))
c = int(input("Write c: "))

result1 = (-b + (b**2 - 4 * a * c)**0.5)/(2*a)
result2 = (-b - (b**2 - 4 * a * c)**0.5)/(2*a)

print("First Result: ", round(result1,5))
print("Second Result: ", round(result2,5))