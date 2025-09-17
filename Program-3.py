a = int(input("Enter a number: "))
if a % 2 == 0:
    n = a - 1
else:
    n = a
for i in range(n):
    print(2*i + 1, end=" ")