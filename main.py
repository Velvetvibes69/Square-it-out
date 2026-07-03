squares = []

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end + 1):
    squares.append(i ** 2)

print("Squared values:", squares)