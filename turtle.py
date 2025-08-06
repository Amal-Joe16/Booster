n = int(input("Enter number of tuples: "))
data = []
for i in range(n):
    # Added missing '.' before split()
    a, b = map(int, input("Enter two integers separated by space: ").split())
    data.append((a, b))

# You don't need to redefine n here; it is already the length of data
# n = len(data)

# Bubble sort to sort tuples by their first element, then by second element if needed
for i in range(n):
    for j in range(0, n - i - 1):
        # Compare first elements of tuples
        if data[j][0] > data[j + 1][0]:
            data[j], data[j + 1] = data[j + 1], data[j]
        # If first elements are equal, compare second elements
        elif data[j][0] == data[j + 1][0] and data[j][1] > data[j + 1][1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("sorted")
print(data)
                