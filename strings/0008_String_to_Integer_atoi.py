class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        num = 0

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            if num > (INT_MAX - digit) // 10:
                return INT_MIN if sign == -1 else INT_MAX

            num = num * 10 + digit
            i += 1

        return sign * num    
