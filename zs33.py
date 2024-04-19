def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("请输入一个正整数："))

if is_prime(n):
    print(f"{n} 是质数")
else:
    print(f"{n} 不是质数")
