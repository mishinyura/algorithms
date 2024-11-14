from typing import Any

class Hash:
    def __init__(self):
        self.table = {}

    def get_hash(self, key: str) -> str:
        hash_size = 64
        for i in key.encode():
            new = f'{i:064b}'
            print(type(new))
            print(new)
        return ''


    def get_index(self):
        pass

    def add(self, idx: int, value: Any) -> None:
        pass

def main():
    eng = 'Hello friend! How are you? Are you woman?'
    rus = 'Привет друг! Как дела? Ты женщина?'
    dt = Hash().get_hash('1234667')
    print(dt)


if __name__ == '__main__':
    main()