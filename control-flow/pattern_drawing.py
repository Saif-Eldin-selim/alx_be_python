num = int(input("Enter the size of the pattern:"))

i = 1
while i <= num:
    for num in range(1, num +1):
        print("*", end="")
    print()
    i=i+1
