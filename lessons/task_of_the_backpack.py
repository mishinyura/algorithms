
class Object:
    def __init__(self, name: str, weight: int, price: float) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Object {self.name}'


class Backpack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.fill = 0

    def put_object(self, obj):
        pass

    def pop_object(self, obj):
        pass

    def d(self, lst: list[Object]):
        pass


def main():
    obj = Object('Фотоаппарат', 2, 300.00)
    obj2 = Object('Телефон', 3, 200.00)
    obj3 = Object('Компьютер', 4, 500.00)
    
