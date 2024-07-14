def main():
    print("Enter the two positive numbers")
    num1 = int(input())
    num2 = int(input())
    gcd = 1
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
    print(f"GCD:{gcd}")

if __name__ == "__main__":
    main()