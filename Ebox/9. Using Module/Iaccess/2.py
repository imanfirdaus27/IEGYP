def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    n = int(input())
    t = int(input())
    for _ in range(t):
        sum = 0
        for i in range(1, n+1):
            if is_prime(i):
                sum += i
        n = sum
    print("Sum:", sum)

if __name__ == '__main__':
    main()