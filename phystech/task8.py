class Node():
    def __init__(self, name: int):
        self.name = name
        self.idx = name - 1
        self._chain = {}

    def __repr__(self):
        return str(self.name)

    def __hash__(self):
        return hash(self.idx)

    @property
    def chain(self) -> dict:
        return self._chain

    @chain.setter
    def chain(self, lst: list[tuple['Node', int]]) -> None:
        for data in lst:
            self._chain.setdefault(data[0], data[1])

    def translate(self) -> list:
        lst = []
        for key, val in self.chain.items():
            lst.insert(key.idx, val)
        lst.insert(self.idx, 0)
        return lst

    def get_min_path(self, ignore: list):
        min_dist = None
        min_obj = None
        for obj, dist in self.chain.items():
            if obj not in ignore:
                if min_dist is not None:
                    if dist < min_dist:
                        min_obj = obj
                else:
                    min_dist = dist
                    min_obj = obj
        return min_obj

class Graph():
    def __init__(self, matrix):
        self.matrix = matrix
        self.__history = []
        self.min_distance = 0
        self.path_min_distance = []

    def __str__(self):
        return f'{self.matrix}'

    def draw(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j]:
                    print(f'({i + 1})--{self.matrix[i][j]}--({j + 1})', end=f' ')
            print()

    def get_min_distance(self, start: Node, end: Node|None=None):
        obj = start
        prev = None
        next = None
        count = 0
        while True:
            next = obj.get_min_path(ignore=self.__history)
            prev = obj
            obj = next
            self.__history.append(prev)
            count += 1
            if count == 4:
                break
        print(self.__history)


def main():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # chains = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]

    node1.chain = [(node2, 10), (node3, 15), (node4, 20)]
    node2.chain = [(node1, 10), (node3, 35), (node4, 25)]
    node3.chain = [(node1, 15), (node2, 35), (node4, 30)]
    node4.chain = [(node1, 20), (node2, 25), (node3, 30)]

    nodes = [node1, node2, node3, node4]
    matrix = []
    for node in nodes:
        matrix.append(node.translate())

    graph = Graph(matrix)
    graph.draw()
    print(graph.get_min_distance(node3))
    # print(graph.get_min_distance(node1))

if __name__ == '__main__':
    main()