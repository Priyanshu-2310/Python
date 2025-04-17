def to_int(s):
    if not isinstance(s, str):
        raise TypeError("only strings are supported for manual conversion")

    s = s.strip()
    if not s:
        raise ValueError("empty string is not supported")

    num = 0
    sign = 1
    i = 0

    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1

    while i < len(s): 
        if '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            num = num * 10 + digit
        else:
            raise ValueError("invalid string")
        i += 1  # Moved outside the if-else to ensure progress

    return sign * num

# Test it
b = to_int("123a")
print(b)  # Output: 123
