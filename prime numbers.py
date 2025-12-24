dividers = []
num = int(input("Enter an integer to find out if it is prime or not: "))
for i in range (1, num + 1):
    if num%i == 0:
        dividers.append(i)
if len(dividers) == 2:
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")
print(f"The dividers of {num} are {dividers}")