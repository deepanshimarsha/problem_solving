def palindrome(x):
    if x == 0:
            return True
    temp = str(x)
    res = ""
    while x > 0:
        digit = str(x%10)
        res = res + digit
        x = x // 10

    if res == temp:
        return "true"
    return "false"

print(palindrome(-121))
