from utils import timer


# TODO

class Solution:
    def __init__(self, test: bool = False) -> None:
        if test:
            self.test_all_solutions()

    @timer
    def isPolindrom1(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    @timer
    def isPolindrom2(self, x: int) -> bool:
        str_num = str(x)
        count = len(str_num)
        for i in range(count // 2):
            if str_num[-i - 1] != str_num[i]:
                return False
            return True

    @timer
    def isPolindrom3(self, x: int) -> bool:
        # Отрицательные числа не палиндромы, числа на 0 кроме 0 — тоже (например, 10)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        # Если длина числа нечётная, откидываем среднюю цифру reverted // 10
        return x == reverted or x == reverted // 10

    def test_all_solutions(self, num: int | None = None) -> None:
        if num is None:
            num = int(input('Введите число: '))

        for name in self.__dir__():
            if name.startswith('__') or name == 'test_all_solutions':
                continue
            method = getattr(self, name)
            if callable(method):
                try:
                    print(method(num))
                except TypeError:
                    pass


def main():
    solution = Solution(True)
    print(0 % 2)


if __name__ == '__main__':
    main()
