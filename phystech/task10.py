
def math_expect(path) -> float:
    with open(path, 'r', encoding='utf-8') as file:
        x = list(map(int, file.readline().split()))
        print(sum(x) / len(x))
        p = list(map(float, file.readline().split()))
        print(sum(p) / len(p))
        result = 0
        for i in range(len(x)):
            result += x[i] * p[i]
        return result

def math_dispersion(lst: list):
    mean = sum(lst) / len(lst)
    dis = [(num - mean) ** 2 for num in lst]
    return sum(dis) / len(lst)

print(math_dispersion([-1, 0, 1, 2]))
print(math_expect('data.txt'))