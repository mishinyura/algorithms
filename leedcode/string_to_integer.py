class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        count = 1
        flag = False
        for ch in s:
            if ch == '-' and count == 1:
                flag = True
                continue
            if ch.isdigit():
                num += int(ch) / 10
                count += 1
            else:
                if count > 1:
                    return num

        if flag:
            num *= -1

        return num

    def myAtoi2(self, s: str) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        s = s.lstrip()
        num = 0
        minus = False

        if not s:
            return 0

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            else:
                if i == '-' and not minus:
                    minus = True
                elif (i.isalpha() or i == '-') and num:
                    return int(num)

        if minus:
            num *= -1
        return int(num)


s = Solution()

print(s.myAtoi2("0-1"))
print(s.myAtoi2("с987"))
print(s.myAtoi2("1337c0d3"))