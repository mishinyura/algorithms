class Object:
    def __init__(self, name: str, weight: int, price: float) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __repr__(self):
        return f'Object {self.name}'

    def __str__(self):
        return self.name


class Backpack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.remain = size
        self.objects = []

    def put_object(self, obj):
        self.objects.append(obj)
        self.remain -= obj.weight


    def pop_object(self, obj):
        index = self.objects.index(obj)
        self.objects.pop(index)
        self.remain += obj.weight

    def search_best_obj(self, lst: list[Object]) -> Object | None:
        if lst:
            best = lst[0]
        else:
            return None
        for obj in lst:
            if obj.price > best.price and obj.weight < best.weight:
                best = obj
        return best


    def get_max_worth(self, *args: Object):
        print(args)
        for obj in args:
            if self.remain >= obj.weight:
                self.put_object(obj)
            else:
                min_price = min([o.price for o in self.objects])

        print(self.objects)



def main():
    obj = Object('Фотоаппарат', 5, 80.00)
    obj2 = Object('Телефон', 3, 50.00)
    obj3 = Object('Компьютер', 7, 100.00)
    backpack = Backpack(10)
    backpack.get_max_worth(obj, obj2, obj3)


if __name__ == '__main__':
    main()