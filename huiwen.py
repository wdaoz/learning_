def is_palindrome(num):
    return str(num) == str(num)[::-1]

# 例如：
number = 121
result = is_palindrome(number)
print(result)