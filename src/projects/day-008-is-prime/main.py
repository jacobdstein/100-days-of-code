def check_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if check_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")