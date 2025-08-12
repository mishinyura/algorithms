class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        prev = 0
        num = 0

        for ch in s[::-1]:
            current = nums[ch]
            if current < prev:
                num -= current
            else:
                num += current
            prev = current
        return num



s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))