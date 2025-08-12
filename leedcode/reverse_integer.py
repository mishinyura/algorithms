class Solution:
    def reverse(self, x: int) -> int:
        new_num = 0

        if x < 0:
            temp = x * -1
        else:
            temp = x

        while temp > 0:
            end_num = temp % 10
            new_num = new_num * 10 + end_num
            temp //= 10
            if temp <= 0 and x < 0:
                new_num *= -1

        print(new_num, 2 ** 31 - 1)
        if new_num < -2 ** 31 or new_num >= 2 ** 31 - 1:
            return 0
        else:
            return new_num

s = Solution()
print(s.reverse(1534236469))
print(s.reverse(-2147483648))