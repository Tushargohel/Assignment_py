x = int(input("Enter a number to check weither its a prime numer or not."))
b = int(x / 2)
for i in range(2, b):
    if x % i == 0:
        print("The number isn't prime.")
    else:
        print("The number is prime.")
